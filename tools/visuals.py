"""Diagram versions of Mindtrek slides 9-15. Run: uv run --with pillow python visuals.py 9"""
import sys
from viz import *


def chain(y, nodes, x0=104, w=316, gap=148, h=112, parts=None, texts=None):
    """Boxes in a row joined by arrows. nodes: (label, icon, sublabel or None, highlight)."""
    for j, (label, ic, sub, hi) in enumerate(nodes):
        bx = x0 + j * (w + gap)
        parts.append(rect(bx, y, w, h, TINT if hi else PANEL, VIOLET if hi else RULE, 2))
        parts.append(icon(ic, bx + 28, y + (h - 52) // 2, 52))
        if sub:
            texts.append((label, bx + 96, y + 18, w - 110, "node"))
            texts.append((sub, bx + 96, y + 58, w - 110, "muted"))
        else:
            texts.append((label, bx + 96, y + (h - lh("node")) // 2, w - 110, "node"))
        if j:
            parts.append(line(bx - gap + 14, y + h // 2, bx - 14, y + h // 2))


def s9():
    k = 9
    clear(k, "From partners to our own server")
    P, T = [], []
    T += [("2013", 104, 462, 110, "year"), ("Client sites on hosting partners' servers.", 214, 462, 1200, "body")]
    chain(520, [("Us", "users", None, False), ("Control panel", "sliders-horizontal", None, False),
                ("Jail", "lock", None, False), ("Their server", "hard-drives", "Apache", False)], parts=P, texts=T)
    P.append(path("M540,646 v14 H1292 v-14", MUTED, 2, head=False))
    T.append(("Jails and control panels stood between us and the server.", 540, 668, 760, "muted"))
    T += [("2015", 104, 744, 110, "year"), ("Our first own VPS, to run the latest nginx and HHVM-FastCGI.", 214, 744, 1400, "body")]
    chain(802, [("Us", "users", None, False), ("SSH", "terminal-window", None, False),
                ("Our own VPS", "hard-drives", "nginx", True)], parts=P, texts=T)
    T.append(("Apache out,\u2028nginx in, for good.", 1412, 826, 400, "body"))
    place(k, "viz-9", render("viz-9", P), T)


def s10():
    k = 10
    clear(k, "Choosing providers, and leaving them")
    P, T = [], []
    stops = [("2015", "cloud", "DigitalOcean", "The first VPS."),
             ("2016", "buildings", "OVH in France", "2 web, 2 database and 1 file server."),
             ("2016", "lightning", "The outage", "Every client\u2028site hangs."),
             ("2016", "moon-stars", "One night", "Every site moved\u2028to a local data\u2028center in Finland."),
             ("2016-2026", "mountains", "The rock cave", "A datacentre in a former army rock cave, on wind power."),
             ("2026", "map-pin", "One provider", "Moving everything to one Finnish provider.")]
    col, ly = 290, 620
    xs = [104 + j * col for j in range(6)]
    P.append(line(104, ly, 1812, ly, RULE, 4, head=False))
    P.append(line(xs[3], ly, 1812, ly, VIOLET, 8, head=False))
    P.append(path(f"M{xs[2] + 14},{ly - 24} C{xs[2] + 110},{ly - 70} {xs[3] - 110},{ly - 70} {xs[3] - 12},{ly - 26}", VIOLET, 3, "8 7"))
    for j, (yr, ic, label, desc) in enumerate(stops):
        x = xs[j]
        P.append(icon(ic, x - 4, 440, 52, INK if j == 2 else VIOLET))
        P.append(circle(x + 11, ly, 12, PANEL if j == 2 else VIOLET, INK if j == 2 else None, 4))
        T.append((yr, x - 4, 512, col - 20, "year"))
        T.append((label, x - 4, 656, col - 20, "node"))
        T.append((desc, x - 4, 700, col - 30, "small"))
    place(k, "viz-10", render("viz-10", P), T)


if __name__ == "__main__":
    for a in sys.argv[1:]:
        globals()["s" + a]()
