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
    stops = [("2015", "cloud", "A US cloud", "The first VPS."),
             ("2016", "buildings", "In France", "2 web, 2 database and 1 file server."),
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


def s11():
    k = 11
    clear(k, "When SSH does not answer")
    P, T = [], []
    rows = [("Monitoring", "heartbeat", "Our checks tell us before a client does.", 450, "back"),
            ("SSH", "terminal-window", "The normal way in. It does not answer.", 550, "broken"),
            ("Console", "monitor", "Screen and keyboard, even with the network down.", 650, "ok"),
            ("Rescue mode", "lifebuoy", "Boot another system and repair the disks.", 750, "ok"),
            ("IPMI", "power", "Power and BIOS on physical servers.", 850, "ok")]
    mx, mw, bh = 470, 760, 86
    # Us
    P.append(rect(104, 407, 240, 486, PANEL, RULE))
    P.append(icon("users", 132, 624, 52))
    T.append(("Us", 200, 650 - lh("node") // 2, 120, "node"))
    # Server
    P.append(rect(1320, 400, 492, 500, TINT, VIOLET))
    for name, y0, y1 in (("Sites", 410, 490), ("Operating system", 510, 690), ("Disks", 710, 790), ("Hardware", 810, 890)):
        P.append(rect(1332, y0, 468, y1 - y0, PANEL, RULE))
        T.append((name, 1360, (y0 + y1) // 2 - lh("node") // 2, 420, "node"))
    for label, ic, desc, cy, kind in rows:
        y = cy - bh // 2
        dash = "10 8" if kind == "broken" else None
        col = INK if kind == "broken" else VIOLET
        P.append(rect(mx, y, mw, bh, PANEL, INK if kind == "broken" else RULE, 2, dash))
        P.append(icon("x-circle" if kind == "broken" else ic, mx + 22, cy - 24, 48, col))
        T.append((label, mx + 90, y + 8, mw - 110, "node"))
        T.append((desc, mx + 90, y + 46, mw - 110, "small"))
        if kind == "back":
            P.append(line(mx - 10, cy, 358, cy, MUTED, 3, "8 7"))
            P.append(line(1320, cy, mx + mw + 12, cy, MUTED, 3, "8 7"))
        else:
            P.append(line(356, cy, mx - 12, cy, col, 3, dash))
            P.append(line(mx + mw + 10, cy, 1318, cy, col, 3, dash))
    place(k, "viz-11", render("viz-11", P), T)


def s12():
    k = 12
    clear(k, "Own servers and the cloud")
    P, T = [], []
    layers = ["Code and data", "Runtime", "Operating system", "Network", "Hardware"]
    cols = [(104, "Own servers", 3,
             "We can open every layer, and moving to another provider means copying files and databases.",
             "We patch, monitor and fix everything ourselves, also at night."),
            (1008, "Cloud", 1,
             "The provider handles hardware failures, failover and scaling.",
             "When the platform breaks, we wait. An American company's EU region still falls under US law.")]
    sw, lh_, gap, top = 396, 74, 8, 452
    for x, title, ours, pro, con in cols:
        T.append((title, x, 388, 500, "label"))
        for j, name in enumerate(layers):
            y = top + j * (lh_ + gap)
            mine = j < ours
            P.append(rect(x, y, sw, lh_, VIOLET if mine else PANEL, None if mine else RULE, 2))
            T.append((name, x + 26, y + (lh_ - lh("nodew")) // 2 - 5, sw - 40, "nodew" if mine else "nodep"))
        tx = x + sw + 40
        P.append(icon("plus-circle", tx, top + 2, 40, VIOLET))
        T.append((pro, tx + 54, top, 318, "small"))
        P.append(icon("minus-circle", tx, top + 212, 40, INK))
        T.append((con, tx + 54, top + 210, 318, "small"))
    P.append(rect(104, 887, 26, 26, VIOLET))
    T.append(("We are in control", 142, 878, 300, "small"))
    P.append(rect(420, 887, 26, 26, PANEL, RULE, 2))
    T.append(("The provider is in control", 458, 878, 400, "small"))
    place(k, "viz-12", render("viz-12", P), T)


if __name__ == "__main__":
    for a in sys.argv[1:]:
        globals()["s" + a]()
