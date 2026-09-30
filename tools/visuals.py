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
    chain(520, [("Agency", "users", None, False), ("Control panel", "sliders-horizontal", None, False),
                ("Jail", "lock", None, False), ("Their server", "hard-drives", "Apache", False)], parts=P, texts=T)
    P.append(path("M540,646 v14 H1292 v-14", MUTED, 2, head=False))
    T.append(("Jails and control panels stood between us and the server.", 540, 668, 760, "muted"))
    T += [("2015", 104, 744, 110, "year"), ("Our first own VPS, to run the latest nginx and HHVM-FastCGI.", 214, 744, 1400, "body")]
    chain(802, [("Agency", "users", None, False), ("SSH", "terminal-window", None, False),
                ("Our own VPS", "hard-drives", "nginx", True)], parts=P, texts=T)
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
    P.append(icon("user", 132, 624, 52))
    T.append(("Admin", 200, 650 - lh("node") // 2, 130, "node"))
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


def s13():
    k = 13
    clear(k, "The fleet today")
    P, T = [], []
    cw, g, bot = 400, 36, 720
    xs = [104 + j * (cw + g) for j in range(4)]
    for j in range(30):
        P.append(icon("hard-drives", xs[0] + (j % 6) * 66, 390 + (j // 6) * 66, 46))
    for j in range(14):
        P.append(icon("user", xs[1] + (j % 5) * 80, 480 + (j // 5) * 80, 56))
    for j, name in enumerate(["nginx", "PHP-FPM", "MariaDB", "Valkey", "fail2ban"]):
        y = 390 + j * 58
        P.append(rect(xs[2], y, cw, 52, PANEL, RULE, 2))
        T.append((name, xs[2] + 22, y + 7, cw - 40, "nodep"))
    P.append(rect(xs[2], 680, cw, 40, VIOLET))
    T.append(("Ubuntu", xs[2] + 22, 681, cw - 40, "nodew"))
    for j, (name, ic) in enumerate([("Analytics", "chart-line"), ("Docs", "files"), ("CRM", "address-book")]):
        y = 390 + j * 114
        P.append(rect(xs[3], y, cw, 102, TINT, VIOLET, 2))
        P.append(icon(ic, xs[3] + 24, y + 27, 48))
        T.append((name, xs[3] + 92, y + (102 - lh("node")) // 2, cw - 110, "node"))
    cells = [("About 30 servers", "Ubuntu on almost all of them."),
             ("14 people", "A web agency with no separate operations team."),
             ("One stack per server", "All on the same machine."),
             ("Own your services", "Analytics, docs and CRM run on our own servers.")]
    for x, (label, body) in zip(xs, cells):
        T.append((label, x, 752, cw, "year"))
        T.append((body, x, 798, cw, "small"))
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
    hx, hy, hw, hh = 1190, 500, 240, 150
    P.append(rect(hx, hy, hw, hh, VIOLET))
    P.append(icon("database", hx + 22, hy + (hh - 56) // 2, 56, PANEL))
    T.append(("Your data", hx + 90, hy + (hh - lh("nodew")) // 2 - 4, 200, "nodew"))
    for j, (label, ic) in enumerate([("Read it", "eye"), ("Back it up", "archive"), ("Move it", "arrow-square-out")]):
        cy = 395 + j * 180
        P.append(rect(1552, cy - 50, 260, 100, PANEL, RULE, 2))
        P.append(icon(ic, 1574, cy - 26, 52))
        T.append((label, 1642, cy - lh("node") // 2, 170, "node"))
        P.append(path(f"M{hx + hw + 10},{hy + hh // 2} C1490,{hy + hh // 2} 1490,{cy} 1540,{cy}", VIOLET, 3))
    place(k, "viz-14", render("viz-14", P), T)


def s15():
    k = 15
    clear(k, "From source and from upstream")
    P, T = [], []
    bh, sx, sw_ = 116, 1120, 692

    def box(x, w, cy, ic, label, desc, fill=PANEL, stroke=RULE):
        y = cy - bh // 2
        P.append(rect(x, y, w, bh, fill, stroke, 2))
        P.append(icon(ic, x + 24, cy - 26, 52))
        T.append((label, x + 94, y + 12, w - 110, "node"))
        T.append((desc, x + 94, y + 50, w - 110, "small"))

    rows = [(460, "file-code", "Module source", "Brotli, cache purging and GeoIP."),
            (600, "download-simple", "Upstream repositories", "nginx.org, the Ondřej Surý PPA\u2028and MariaDB."),
            (740, "package", "Distribution packages", "Everything else\u2028comes from Ubuntu.")]
    for cy, ic, label, desc in rows:
        box(104, 500, cy, ic, label, desc)
    box(680, 340, 460, "wrench", "Built here", "Against the exact\u2028nginx that runs.", TINT, VIOLET)
    P.append(line(616, 460, 668, 460))
    P.append(line(1032, 460, sx - 12, 460))
    for cy in (600, 740):
        P.append(line(616, cy, sx - 12, cy))
    P.append(rect(sx, 400, sw_, 400, TINT, VIOLET, 2))
    P.append(icon("hard-drives", sx + 28, 424, 56))
    for j, chip in enumerate(["nginx and modules", "PHP", "MariaDB", "Ubuntu packages"]):
        cx, cy2 = sx + 28 + (j % 2) * 324, 510 + (j // 2) * 66
        P.append(rect(cx, cy2, 308, 52, PANEL, RULE, 2))
        T.append((chip, cx + 18, cy2 + 7, 280, "nodep"))
    T.append(("Our server", sx + 100, 432, 400, "node"))
    P.append(rect(sx + 14, 660, sw_ - 28, 126, VIOLET))
    T.append(("Configured by hand", sx + 40, 672, sw_ - 80, "nodew"))
    T.append(("Every configuration file is ours,\u2028with our own defaults.", sx + 40, 714, sw_ - 80, "smallw"))
    place(k, "viz-15", render("viz-15", P), T)


def standards(k):
    """New slide after node_modules: self-hosting still needs standards."""
    P, T = [], []
    bh = 116

    def box(x, w, cy, ic, label, desc, fill=PANEL, stroke=RULE, h=bh):
        y = cy - h // 2
        P.append(rect(x, y, w, h, fill, stroke, 2))
        P.append(icon(ic, x + 24, cy - 26, 52))
        T.append((label, x + 94, cy - 46, w - 110, "node"))
        T.append((desc, x + 94, cy - 8, w - 110, "small"))

    for (cy, ic, label, desc), ty in zip([(460, "file-code", "Built from source", "Where the details matter."),
                                (600, "list-checks", "Ansible playbooks", "The same setup on every server."),
                                (740, "cube", "Docker", "For some services, where it fits.")], (560, 600, 640)):
        box(104, 500, cy, ic, label, desc)
        P.append(line(616, cy, 728, ty))
    box(740, 420, 600, "check-circle", "One standard", "Several ways to do it,\u2028each one agreed on.", TINT, VIOLET, 180)
    P.append(line(1172, 600, 1268, 600))
    y = 510
    P.append(rect(1280, y, 532, 180, VIOLET))
    P.append(icon("book-open-text", 1304, 574, 52, PANEL))
    T.append(("Written down", 1374, 554, 420, "nodew"))
    T.append(("Servers and code are\u2028both documented.", 1374, 592, 420, "smallw"))
    place(k, f"viz-{k}", render(f"viz-{k}", P), T)


def portability(k):
    P, T = [], []
    P.append(rect(104, 400, 560, 420, TINT, VIOLET, 2))
    for j, (label, ic) in enumerate([("Open source software", "file-code"), ("Your own servers", "hard-drives"),
                                     ("Your own data", "database"), ("Open APIs", "brackets-curly")]):
        y = 418 + j * 100
        P.append(rect(122, y, 524, 84, PANEL, RULE, 2))
        P.append(icon(ic, 146, y + 18, 48))
        T.append((label, 214, y + (84 - lh("node")) // 2, 420, "node"))
    targets = [(470, "truck", "Another provider", "Copy the files and databases, and go."),
               (610, "robot", "Any tool, with AI", "With a proper API, an MCP server can\u2028move data in any direction."),
               (750, "eye-slash", "Nobody watching", "Nobody can spy on data that sits\u2028on your own servers.")]
    for cy, ic, label, desc in targets:
        y = cy - 58
        P.append(rect(1140, y, 672, 116, PANEL, RULE, 2))
        P.append(icon(ic, 1164, cy - 26, 52))
        T.append((label, 1234, cy - 46, 560, "node"))
        T.append((desc, 1234, cy - 8, 560, "small"))
        priv = ic == "eye-slash"
        P.append(line(686, 610 + (cy - 610) // 3, 1126, cy, MUTED if priv else VIOLET, 3, "8 7" if priv else None, head=not priv, both=not priv))
    place(k, f"viz-{k}", render(f"viz-{k}", P), T)


if __name__ == "__main__":
    for a in sys.argv[1:]:
        globals()["s" + a]()
