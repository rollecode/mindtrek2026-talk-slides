"""Diagram versions of Mindtrek slides 9-16 and 23. Run: uv run --with pillow python visuals.py 9 10"""
import sys
from viz import *


def chain(P, T, y, nodes, x0=104, w=316, gap=148, h=104):
    """Boxes in a row joined by arrows. nodes: (label, icon, sublabel or None, highlight)."""
    for j, (label, ic, sub, hi) in enumerate(nodes):
        bx = x0 + j * (w + gap)
        box(P, T, bx, y, w, h, ic, label, sub, fill=TINT if hi else PANEL, stroke=VIOLET if hi else RULE, ds="muted")
        if j:
            P.append(line(bx - gap + 16, y + h // 2, bx - 16, y + h // 2))


def s9():
    k = 9
    clear(k, "From partners\u2028to our own server")
    P, T = [], []
    T += [("2013", 104, 466, 110, "year"), ("Client sites on hosting partners' servers.", 206, 466, 1200, "body")]
    chain(P, T, 522, [("Agency", "users", None, False), ("Control panel", "sliders-horizontal", None, False),
                      ("Jail", "lock", None, False), ("Their server", "hard-drives", "Apache", False)])
    P.append(path("M540,646 v14 H1292 v-14", MUTED, 2, head=False))
    T.append(("Jails and control panels stood between us and the server.", 540, 670, 760, "muted"))
    T += [("2015", 104, 748, 110, "year"), ("Our first own VPS, to run the latest nginx and HHVM-FastCGI.", 206, 748, 1400, "body")]
    chain(P, T, 804, [("Agency", "users", None, False), ("SSH", "terminal-window", None, False),
                      ("Our own VPS", "hard-drives", "nginx", True)])
    place(k, "viz-9", render("viz-9", P), T)


def s10():
    k = 10
    clear(k, "Choosing providers, and leaving them")
    P, T = [], []
    stops = [("2015", "cloud", "A US cloud", "The first VPS."),
             ("2016", "buildings", "In France", "2 web, 2 database and 1 file server."),
             ("2016", "lightning", "The outage", "Every client site hangs."),
             ("2016", "moon-stars", "One night", "Every site moved to a local data center in Finland."),
             ("2016-2026", "mountains", "The rock cave", "A datacentre in a former army rock cave, on wind power."),
             ("2026", "map-pin", "One provider", "Moving everything to one Finnish provider.")]
    col, ly = 290, 620
    xs = [104 + j * col for j in range(6)]
    P.append(line(104, ly, 1812, ly, VIOLET, 4, head=False))
    P.append(path(f"M{xs[2] + 14},{ly - 24} C{xs[2] + 110},{ly - 70} {xs[3] - 110},{ly - 70} {xs[3] - 12},{ly - 26}", VIOLET, 3, "8 7"))
    for j, (yr, ic, label, desc) in enumerate(stops):
        x = xs[j]
        P.append(icon(ic, x - 2, 448, 44, INK if j == 2 else VIOLET))
        P.append(circle(x + 11, ly, 12, PANEL if j == 2 else VIOLET, INK if j == 2 else None, 4))
        T.append((yr, x - 4, 516, col - 20, "year"))
        T.append((label, x - 4, 660, col - 20, "node"))
        T.append((desc, x - 4, 702, col - 40, "small"))
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
    mx, mw, bh = 470, 760, 78
    box(P, T, 104, 411, 240, 478, "user", "Admin")
    P.append(rect(1320, 400, 492, 500, TINT, VIOLET))
    for name, y0, y1 in (("Sites", 414, 488), ("Operating system", 514, 686), ("Disks", 714, 788), ("Hardware", 814, 888)):
        P.append(rect(1334, y0, 464, y1 - y0, PANEL, RULE))
        T.append((name, 1362, (y0 + y1) // 2 - lh("nodep") // 2 - 2, 420, "nodep"))
    for label, ic, desc, cy, kind in rows:
        broken = kind == "broken"
        dash = "10 8" if broken else None
        col = INK if broken else VIOLET
        box(P, T, mx, cy - bh // 2, mw, bh, "x-circle" if broken else ic, label, desc,
            stroke=INK if broken else RULE, dash=dash, icol=col, isz=40)
        if kind == "back":
            P.append(line(mx - 12, cy, 358, cy, MUTED, 3, "8 7"))
            P.append(line(1320, cy, mx + mw + 14, cy, MUTED, 3, "8 7"))
        else:
            P.append(line(356, cy, mx - 14, cy, col, 3, dash))
            P.append(line(mx + mw + 12, cy, 1318, cy, col, 3, dash))
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
    sw, bh, gap, top = 396, 66, 16, 452
    for x, title, ours, pro, con in cols:
        T.append((title, x, 388, 500, "label"))
        for j, name in enumerate(layers):
            y = top + j * (bh + gap)
            mine = j < ours
            P.append(rect(x, y, sw, bh, VIOLET if mine else PANEL, None if mine else RULE, 2))
            T.append((name, x + 28, y + (bh - lh("nodew")) // 2 - 2, sw - 56, "nodew" if mine else "nodep"))
        tx = x + sw + 44
        P.append(icon("plus-circle", tx, top + 2, 36, VIOLET))
        T.append((pro, tx + 52, top, 300, "small"))
        P.append(icon("minus-circle", tx, top + 212, 36, INK))
        T.append((con, tx + 52, top + 210, 300, "small"))
    P.append(rect(104, 892, 24, 24, VIOLET))
    T.append(("We are in control", 140, 884, 300, "small"))
    P.append(rect(420, 892, 24, 24, PANEL, RULE, 2))
    T.append(("The provider is in control", 456, 884, 400, "small"))
    place(k, "viz-12", render("viz-12", P), T)


def s13():
    k = 13
    clear(k, "The fleet today")
    P, T = [], []
    cw, g = 400, 36
    xs = [104 + j * (cw + g) for j in range(4)]
    for j in range(30):
        P.append(icon("hard-drives", xs[0] + (j % 6) * 66, 392 + (j // 6) * 66, 42))
    for j in range(14):
        P.append(icon("user", xs[1] + (j % 5) * 80, 488 + (j // 5) * 80, 50))
    for j, name in enumerate(["nginx", "PHP-FPM", "MariaDB", "Valkey", "fail2ban"]):
        y = 390 + j * 56
        P.append(rect(xs[2], y, cw, 44, PANEL, RULE, 2))
        T.append((name, xs[2] + 24, y + (44 - lh("nodep")) // 2 - 2, cw - 48, "nodep"))
    P.append(rect(xs[2], 674, cw, 44, VIOLET))
    T.append(("Ubuntu", xs[2] + 24, 674 + (44 - lh("nodew")) // 2 - 2, cw - 48, "nodew"))
    for j, (name, ic) in enumerate([("Analytics", "chart-line"), ("Docs", "files"), ("CRM", "address-book")]):
        box(P, T, xs[3], 390 + j * 112, cw, 92, ic, name, fill=TINT, stroke=VIOLET)
    cells = [("About 30 servers", "Ubuntu on almost all of them."),
             ("14 people", "A web agency with no separate operations team."),
             ("One stack per server", "All on the same machine."),
             ("Own your services", "Analytics, docs and CRM run on our own servers.")]
    for x, (label, body) in zip(xs, cells):
        T.append((label, x, 758, cw, "year"))
        T.append((body, x, 802, cw - 20, "small"))
    place(k, "viz-13", render("viz-13", P), T)


def s14():
    k = 14
    d = n.dump(k)
    assert [x["text"] for x in d[:2]] == ["Own your data", "and know where it lives"], d[:2]
    n.osa(f'''tell application "Keynote" to tell slide {k} of document {n.q(n.DOC)}
  repeat with i from (count of images) to 1 by -1
    if file name of image i starts with "viz-" then delete image i
  end repeat
  repeat with i from (count of text items) to 1 by -1
    if (object text of text item i as text) is in {{"Our data", "Your data", "Read it", "Back it up", "Move it"}} then delete text item i
  end repeat
  set t to text item 3
  set p to position of t
  set width of t to 820
  set position of t to p
end tell''')
    P, T = [], []
    hx, hy, hw, hh = 1190, 505, 240, 140
    box(P, T, hx, hy, hw, hh, "database", "Your data", fill=VIOLET, stroke=None, icol=PANEL, ls="nodew")
    for j, (label, ic) in enumerate([("Read it", "eye"), ("Back it up", "archive"), ("Move it", "arrow-square-out")]):
        cy = 405 + j * 170
        box(P, T, 1552, cy - 44, 260, 88, ic, label)
        P.append(path(f"M{hx + hw + 12},{hy + hh // 2} C1490,{hy + hh // 2} 1490,{cy} 1538,{cy}", VIOLET, 3))
    place(k, "viz-14", render("viz-14", P), T)


def s15():
    k = 15
    clear(k, "Move anywhere, any time")
    P, T = [], []
    P.append(rect(104, 404, 560, 412, TINT, VIOLET, 2))
    for j, (label, ic) in enumerate([("Open source software", "file-code"), ("Your own servers", "hard-drives"),
                                     ("Your own data", "database"), ("Open APIs", "brackets-curly")]):
        box(P, T, 124, 424 + j * 98, 520, 78, ic, label)
    targets = [(470, "truck", "Another provider", "Copy the files and databases, and go.", 1),
               (610, "robot", "Any tool, with AI", "With a proper API, an MCP server can move data in any direction.", 2),
               (750, "eye-slash", "Nobody watching", "Nobody can spy on data that sits on your own servers.", 2)]
    for cy, ic, label, desc, nl in targets:
        box(P, T, 1140, cy - 56, 672, 112, ic, label, desc, nl)
        priv = ic == "eye-slash"
        P.append(line(686, 610 + (cy - 610) // 3, 1124, cy, MUTED if priv else VIOLET, 3,
                      "8 7" if priv else None, head=not priv, both=not priv))
    place(k, f"viz-{k}", render(f"viz-{k}", P), T)


def s16():
    k = 16
    clear(k, "From source and from upstream")
    P, T = [], []
    bh, sx, sw_ = 108, 1120, 692
    rows = [(460, "file-code", "Module source", "Brotli, cache purging and GeoIP.", 1),
            (600, "download-simple", "Upstream repositories", "nginx.org, the Ondřej Surý PPA and MariaDB.", 2),
            (740, "package", "Distribution packages", "Everything else comes from Ubuntu.", 2)]
    for cy, ic, label, desc, nl in rows:
        box(P, T, 104, cy - bh // 2, 500, bh, ic, label, desc, nl)
    box(P, T, 680, 460 - bh // 2, 340, bh, "wrench", "Built here", "Against the exact nginx that runs.", 2,
        fill=TINT, stroke=VIOLET)
    P.append(line(618, 460, 666, 460))
    P.append(line(1034, 460, sx - 14, 460))
    for cy in (600, 740):
        P.append(line(618, cy, sx - 14, cy))
    P.append(rect(sx, 400, sw_, 400, TINT, VIOLET, 2))
    P.append(icon("hard-drives", sx + 28, 424, 48))
    T.append(("Our server", sx + 96, 428, 400, "node"))
    for j, chip in enumerate(["nginx and modules", "PHP", "MariaDB", "Ubuntu packages"]):
        cx, cy2 = sx + 28 + (j % 2) * 324, 498 + (j // 2) * 62
        P.append(rect(cx, cy2, 308, 46, PANEL, RULE, 2))
        T.append((chip, cx + 20, cy2 + (46 - lh("nodep")) // 2 - 2, 276, "nodep"))
    P.append(rect(sx + 16, 648, sw_ - 32, 136, VIOLET))
    T.append(("Configured by hand", sx + 44, 666, sw_ - 88, "nodew"))
    T.append(("Every configuration file is ours, with our own defaults.", sx + 44, 706, sw_ - 88, "smallw"))
    place(k, "viz-16", render("viz-16", P), T)


def s23():
    k = 23
    clear(k, "Self-hosting needs standards too")
    P, T = [], []
    bh = 108
    for (cy, ic, label, desc), ty in zip([(460, "file-code", "Built from source", "Where the details matter."),
                                          (600, "list-checks", "Ansible playbooks", "The same setup on every server."),
                                          (740, "cube", "Docker", "For some services, where it fits.")], (560, 600, 640)):
        box(P, T, 104, cy - bh // 2, 500, bh, ic, label, desc)
        P.append(line(618, cy, 726, ty))
    box(P, T, 740, 515, 420, 170, "check-circle", "One standard", "Several ways to do it, each one agreed on.", 2,
        fill=TINT, stroke=VIOLET)
    P.append(line(1174, 600, 1266, 600))
    box(P, T, 1280, 515, 532, 170, "book-open-text", "Written down", "Servers and code are both documented.", 2,
        fill=VIOLET, stroke=None, icol=PANEL, ls="nodew", ds="smallw")
    place(k, f"viz-{k}", render(f"viz-{k}", P), T)


if __name__ == "__main__":
    for a in sys.argv[1:]:
        globals()["s" + a]()
