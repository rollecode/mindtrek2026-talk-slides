"""Diagrams for the Mindtrek deck: shapes and icons as one cropped PNG, every word as editable Keynote text."""
import os, re, subprocess, tempfile
from PIL import Image
import newsection as n

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "keyassets", "viz")
PH = "/private/tmp/claude-501/-Users-rolle-Projects-keynote-base/c26984b9-15ab-4610-9987-b4f97c97e0e0/scratchpad/ph/package/assets"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

INK, VIOLET, BODY, MUTED = "#190834", "#4C1D95", "#2E1B34", "#8A7BA8"
PANEL, TINT, RULE = "#FFFFFF", "#E6DEFA", "#C9BCEB"

# Keynote styles: font, size, colour as 16-bit RGB.
def _rgb(h):
    return "{" + ", ".join(str(int(h[i:i + 2], 16) * 257) for i in (1, 3, 5)) + "}"

STYLES = {
    "label": ("Unbounded-Regular_SemiBold", 34, _rgb(VIOLET)),
    "big": ("Unbounded-Regular_ExtraBold", 96, _rgb(INK)),
    "year": ("Unbounded-Regular_SemiBold", 30, _rgb(VIOLET)),
    "node": ("Geist-SemiBold", 30, _rgb(INK)),
    "nodew": ("Geist-SemiBold", 28, _rgb("#FFFFFF")),
    "nodep": ("Geist-SemiBold", 28, _rgb(INK)),
    "body": ("Geist-Regular", 30, _rgb(BODY)),
    "small": ("Geist-Regular", 25, _rgb(BODY)),
    "muted": ("Geist-Regular", 25, _rgb(MUTED)),
    "mono": ("GeistMono-Regular", 24, _rgb(BODY)),
}


def icon(name, x, y, s=56, color=VIOLET, weight="regular"):
    f = name if weight == "regular" else f"{name}-{weight}"
    svg = open(f"{PH}/{weight}/{f}.svg").read()
    inner = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S).group(1)
    return f'<svg x="{x}" y="{y}" width="{s}" height="{s}" viewBox="0 0 256 256" fill="{color}">{inner}</svg>'


def rect(x, y, w, h, fill=PANEL, stroke=None, sw=2, dash=None):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    if dash:
        st += f' stroke-dasharray="{dash}"'
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"{st}/>'


def line(x1, y1, x2, y2, color=VIOLET, sw=3, dash=None, head=True):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#h{color[1:]})"' if head else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"{d}{m}/>'


def path(d, color=VIOLET, sw=3, dash=None, head=True, fill="none"):
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#h{color[1:]})"' if head else ""
    return f'<path d="{d}" stroke="{color}" stroke-width="{sw}" fill="{fill}"{ds}{m}/>'


def circle(cx, cy, r, fill=VIOLET, stroke=None, sw=3):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{st}/>'


def _markers():
    return "".join(
        f'<marker id="h{c[1:]}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="16" markerHeight="16" '
        f'markerUnits="userSpaceOnUse" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
        for c in (INK, VIOLET, MUTED, RULE))


def render(name, parts):
    """Render SVG parts on a 1920x1080 transparent page at 2x; crop; return the slide box."""
    os.makedirs(OUT, exist_ok=True)
    html = (f'<html><body style="margin:0;background:transparent"><svg xmlns="http://www.w3.org/2000/svg" '
            f'width="1920" height="1080"><defs>{_markers()}</defs>{"".join(parts)}</svg></body></html>')
    with tempfile.TemporaryDirectory() as t:
        src, shot = f"{t}/p.html", f"{t}/p.png"
        open(src, "w").write(html)
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--screenshot={shot}",
                        "--window-size=1920,1080", "--force-device-scale-factor=2",
                        "--default-background-color=00000000", f"file://{src}"], capture_output=True, check=True)
        im = Image.open(shot).convert("RGBA")
    l, t_, r, b = im.getbbox()
    l, t_ = l // 2 * 2, t_ // 2 * 2
    im.crop((l, t_, r, b)).save(f"{OUT}/{name}.png")
    return l // 2, t_ // 2, (r - l + 1) // 2, (b - t_ + 1) // 2


def clear(k, keep_heading):
    """Delete body text and old diagrams on slide k; keep the heading, footer and placeholders."""
    D = n.q(n.DOC)
    assert n.dump(k)[0]["text"] == keep_heading, n.dump(k)[0]["text"]
    n.osa(f'''tell application "Keynote" to tell slide {k} of document {D}
  repeat with i from (count of text items) to 2 by -1
    set v to object text of text item i as text
    if v is not "" and v is not "Sovereign by habit" then delete text item i
  end repeat
  repeat with i from (count of images) to 1 by -1
    if file name of image i starts with "viz-" then delete image i
  end repeat
end tell''')


def place(k, name, box, texts):
    """Put the diagram image and then its texts [(text, x, y, w, style)] on slide k."""
    D = n.q(n.DOC)
    x, y, w, h = box
    lines = [f'make new image with properties {{file:(POSIX file {n.q(os.path.abspath(OUT + "/" + name + ".png"))}), '
             f'position:{{{x}, {y}}}, width:{w}, height:{h}}}']
    for s, tx, ty, tw, st in texts:
        f, z, c = STYLES[st]
        lines.append(f'''set t to make new text item with properties {{object text:{n.q(s)}, position:{{{tx}, {ty}}}, width:{tw}}}
  tell object text of t
    set its font to "{f}"
    set its size to {z}
    set its color to {c}
  end tell
  set position of t to {{{tx}, {ty}}}''')
    n.osa(f'tell application "Keynote" to tell slide {k} of document {D}\n  ' + "\n  ".join(lines) + "\nend tell")
    n.osa(f'tell application "Keynote" to save document {D}')


def lh(style):
    """Approximate Keynote line box height for a style, to centre text in shapes."""
    return round(STYLES[style][1] * 1.3)
