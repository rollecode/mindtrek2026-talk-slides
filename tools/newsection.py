"""Edit the live Going ACF-free deck in Keynote: dump slides, clone layouts, set text."""
import subprocess, sys

DOC = "Sovereign by habit.key"
INK = "{6425, 2056, 13364}"
VIOLET = "{19532, 7453, 38293}"


def osa(script):
    r = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"osascript failed: {r.stderr}\n--- script ---\n{script[:1500]}")
    return r.stdout.rstrip("\n")


def q(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def ql(s):
    return " & return & ".join(q(x) for x in s.split("\n"))


# Heading text of a slide whose layout gets cloned; Rolle renames slides, so override as needed.
MARKERS = {
    "statement": "True dependency-free WordPress",
    "pairs": "From core to custom, prioritized",
    "quote": "What is a dependency?",
}


def find_slide(marker):
    """First slide with a text item that starts with marker; 0 if none."""
    return int(osa(f'''tell application "Keynote"
  set d to document {q(DOC)}
  repeat with n from 1 to (count of slides of d)
    repeat with t in (text items of slide n of d)
      if (object text of t as text) starts with {q(marker)} then return n
    end repeat
  end repeat
  return 0
end tell''').strip())


def dump(n):
    out = osa(f'''tell application "Keynote"
  set s to slide {n} of document {q(DOC)}
  set RS to character id 30
  set US to character id 31
  set out to ""
  repeat with i from 1 to (count of text items of s)
    set t to text item i of s
    set v to object text of t as text
    set p to position of t
    set out to out & i & US & (font of object text of t) & US & ((size of object text of t) as integer) & US & ((item 1 of p) as integer) & US & ((item 2 of p) as integer) & US & v & RS
  end repeat
  return out
end tell''')
    items = []
    for rec in out.split("\x1e"):
        if not rec.strip():
            continue
        i, f, z, x, y, v = rec.split("\x1f", 5)
        items.append(dict(i=int(i), font=f, size=int(z), x=int(x), y=int(y), text=v))
    return items


def set_text(n, i, text, restyle_from=None):
    """Replace text keeping position; optionally restyle an em run for one-line headings."""
    em = ""
    if restyle_from:
        em = f'''
    tell object text of t
      set its font to "Unbounded-Regular_ExtraBold"
      set its size to 76
      set its color to {INK}
    end tell
    tell characters {restyle_from} thru {len(text)} of object text of t
      set its font to "InstrumentSerif-Italic"
      set its size to 98
      set its color to {VIOLET}
    end tell'''
    osa(f'''tell application "Keynote"
  set t to text item {i} of slide {n} of document {q(DOC)}
  set p to position of t
  set object text of t to {q(text)}{em}
  set position of t to p
end tell''')


def build(spec, pos):
    """Duplicate a layout slide to after slide pos and fill it; returns the new slide number."""
    lay = spec["layout"]
    src = find_slide(MARKERS[lay])
    if not src or not pos:
        sys.exit(f"source for {lay} ({src}) or position ({pos}) not found")
    osa(f'tell application "Keynote" to duplicate slide {src} of document {q(DOC)} to after slide {pos} of document {q(DOC)}')
    n = pos + 1
    items = [it for it in dump(n) if it["text"] not in ("", "Going ACF-free")]

    def heading_one_line(head, em):
        h = next(it for it in items if it["font"] == "Unbounded-Regular_ExtraBold" and it["size"] == 76)
        set_text(n, h["i"], f"{head} {em}", restyle_from=len(head) + 2)

    if lay == "statement":
        head_item = next(it for it in items if it["font"] == "Unbounded-Regular_ExtraBold")
        em_item = next(it for it in items if it["font"] == "InstrumentSerif-Italic")
        set_text(n, head_item["i"], spec["head"])
        set_text(n, em_item["i"], spec["em"])
        sf = sorted((it for it in items if it["font"].startswith("Geist")), key=lambda it: it["y"])
        for it, line in zip(sf, spec["standfirst"]):
            set_text(n, it["i"], line)
        # The template's heading wraps to two lines; a one-line heading needs the
        # approved spacing (slides 9, 14, 25): italic = heading + 92, text = italic + 184.
        ys = [(head_item, 331), (em_item, 423)] + [(it, 607 + k * 52) for k, it in enumerate(sf)]
        for it, y in ys:
            osa(f'tell application "Keynote" to tell text item {it["i"]} of slide {n} of document {q(DOC)}\nset p to position\nset position to {{item 1 of p, {y}}}\nend tell')
    elif lay == "pairs":
        heading_one_line(spec["head"], spec["em"])
        labels = sorted((it for it in items if it["font"] == "Unbounded-Regular_SemiBold"), key=lambda it: (it["y"], it["x"]))
        bodies = sorted((it for it in items if it["font"].startswith("Geist") and it["size"] >= 30), key=lambda it: (it["y"], it["x"]))
        for it, (label, _) in zip(labels, spec["pairs"]):
            set_text(n, it["i"], label)
        for it, (_, body) in zip(bodies, spec["pairs"]):
            set_text(n, it["i"], body)
        # The template's last cell is inline code; make every body plain Geist.
        if bodies:
            ref = bodies[0]["i"]
            for it in bodies[1:]:
                osa(f'''tell application "Keynote" to tell slide {n} of document {q(DOC)}
  set z to size of object text of text item {ref}
  set c to color of object text of text item {ref}
  set t to text item {it["i"]}
  set p to position of t
  tell object text of t
    set its font to "Geist-Regular"
    set its size to z
    set its color to c
  end tell
  set position of t to p
end tell''')
    osa(f'tell application "Keynote" to set presenter notes of slide {n} of document {q(DOC)} to {ql(spec["notes"])}')
    return n
