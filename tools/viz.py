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
    "label": ("Unbounded-Regular_SemiBold", 32, _rgb(VIOLET)),
    "big": ("Unbounded-Regular_ExtraBold", 96, _rgb(INK)),
    "year": ("Unbounded-Regular_SemiBold", 28, _rgb(VIOLET)),
    "node": ("Geist-SemiBold", 26, _rgb(INK)),
    "nodew": ("Geist-SemiBold", 25, _rgb("#FFFFFF")),
    "nodep": ("Geist-SemiBold", 25, _rgb(INK)),
    "label22": ("Geist-SemiBold", 22, _rgb(INK)),
    "label22w": ("Geist-SemiBold", 22, _rgb("#FFFFFF")),
    "desc20": ("Geist-Regular", 20, _rgb(BODY)),
    "desc20w": ("Geist-Regular", 20, _rgb("#FFFFFF")),
    "colhead": ("Unbounded-Regular_SemiBold", 42, _rgb(VIOLET)),
    "colsub": ("Geist-Regular", 26, _rgb(MUTED)),
    "tipnum": ("Unbounded-Regular_SemiBold", 34, _rgb(VIOLET)),
    "tip30": ("Geist-Regular", 30, _rgb(BODY)),
    "tip": ("Geist-Regular", 24, _rgb(BODY)),
    "chip": ("Geist-SemiBold", 22, _rgb(INK)),
    "chipw": ("Geist-SemiBold", 22, _rgb("#FFFFFF")),
    "smallw": ("Geist-Regular", 22, _rgb("#FFFFFF")),
    "body": ("Geist-Regular", 28, _rgb(BODY)),
    "small": ("Geist-Regular", 22, _rgb(BODY)),
    "muted": ("Geist-Regular", 22, _rgb(MUTED)),
    "mono": ("GeistMono-Regular", 22, _rgb(BODY)),
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


def line(x1, y1, x2, y2, color=VIOLET, sw=3, dash=None, head=True, both=False):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#h{color[1:]})"' if head else ""
    if both:
        m += f' marker-start="url(#h{color[1:]})"'

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
    """Write every part as its own SVG file, cropped to its measured box; return [(file, x, y, w, h)]."""
    import json
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        if f.startswith(name + "-") and f.endswith(".svg"):
            os.remove(f"{OUT}/{f}")
    defs = _markers()
    body = "".join(f'<g id="p{j}">{p}</g>' for j, p in enumerate(parts))
    html = (f'<html><body style="margin:0"><svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080">'
            f'<defs>{defs}</defs>{body}</svg><pre id="out"></pre><script>'
            f'var r=[];for(var j=0;j<{len(parts)};j++){{var b=document.getElementById("p"+j).getBoundingClientRect();'
            f'r.push([b.left,b.top,b.width,b.height]);}}document.getElementById("out").textContent=JSON.stringify(r);'
            f'</script></body></html>')
    with tempfile.TemporaryDirectory() as t:
        src = f"{t}/p.html"
        open(src, "w").write(html)
        dom = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--dump-dom", f"file://{src}"],
                             capture_output=True, text=True, check=True).stdout
    boxes = json.loads(re.search(r'<pre id="out">(.*?)</pre>', dom, re.S).group(1))
    out = []
    for j, (p, (bx, by, bw, bh)) in enumerate(zip(parts, boxes)):
        pad = 12
        x, y = int(bx) - pad, int(by) - pad
        w, h = int(bw + (bx - int(bx))) + 2 * pad + 1, int(bh + (by - int(by))) + 2 * pad + 1
        f = f"{OUT}/{name}-{j:02d}.svg"
        open(f, "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
                           f'viewBox="{x} {y} {w} {h}"><defs>{defs}</defs>{p}</svg>')
        out.append((f, x, y, w, h))
    return out


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


def place(k, name, items, texts):
    """Put each diagram part as its own image, then the texts [(text, x, y, w, style)], on slide k."""
    D = n.q(n.DOC)
    lines = [f'make new image with properties {{file:(POSIX file {n.q(os.path.abspath(f))}), '
             f'position:{{{x}, {y}}}, width:{w}, height:{h}}}' for f, x, y, w, h in items]
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


def box(P, T, x, y, w, h, ic, label, desc=None, lines=1, fill=PANEL, stroke=RULE, dash=None,
        icol=VIOLET, ls="node", ds="small", isz=44):
    """A box with an icon and a label, optionally a description, centred vertically with even padding."""
    P.append(rect(x, y, w, h, fill, stroke, 2, dash) if stroke else rect(x, y, w, h, fill))
    P.append(icon(ic, x + 28, y + (h - isz) // 2, isz, icol))
    tx, tw = x + 28 + isz + 22, w - (28 + isz + 22) - 24
    if desc:
        top = y + (h - (lh(ls) + 4 + lines * round(STYLES[ds][1] * 1.25))) // 2 - 2
        T.append((label, tx, top, tw, ls))
        T.append((desc, tx, top + lh(ls) + 4, tw, ds))
    else:
        T.append((label, tx, y + (h - lh(ls)) // 2 - 2, tw, ls))
