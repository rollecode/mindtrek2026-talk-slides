"""Diagram versions of Mindtrek slides 9-12, 14, 16 and 19-21. Run: uv run --with pillow python visuals.py 9 10"""
import sys
from viz import *
from viz import _rgb


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
    P.append(path("M568,642 v14 H1348 v-14", MUTED, 2, head=False))
    T.append(("Jails and control panels stood between us and the server.", 568, 666, 780, "muted"))
    T += [("2015", 104, 748, 110, "year"), ("Our first own VPS, to run the latest nginx and HHVM-FastCGI.", 206, 748, 1400, "body")]
    chain(P, T, 804, [("Agency", "users", None, False), ("SSH", "terminal-window", None, False),
                      ("Our own VPS", "hard-drives", "nginx", True)])
    place(k, "viz-9", render("viz-9", P), T)


def s10():
    k = 10
    clear(k, "Choosing providers, and leaving them")
    P, T = [], []
    stops = [("2015", "cloud", "A US cloud", "The first VPS."),
             ("2016", "buildings", "In France", "2 web, 2 database\u2028and 1 file server."),
             ("2016", "lightning", "The outage", "Every client\u2028site hangs."),
             ("2016", "truck", "The move", "Every site moved\u2028to a local data\u2028center in Finland."),
             ("Since 2016", "mountains", "The rock cave", "A datacentre in a\u2028former army rock\u2028cave, on wind power."),
             ("2026", "map-pin", "Today", "Still on European\u2028servers, data on sovereign ground.")]
    col, ly = 290, 620
    xs = [104 + j * col for j in range(6)]
    P.append(line(104, ly, 1812, ly, VIOLET, 4, head=False))
    P.append(path(f"M{xs[2] + 14},{ly - 24} C{xs[2] + 110},{ly - 70} {xs[3] - 110},{ly - 70} {xs[3] - 12},{ly - 26}", VIOLET, 3, "8 7"))
    for j, (yr, ic, label, desc) in enumerate(stops):
        x = xs[j]
        P.append(icon(ic, x - 2, 448, 44))
        P.append(circle(x + 11, ly, 12))
        T.append((yr, x - 4, 516, col - 20, "year"))
        T.append((label, x - 4, 660, col - 20, "node"))
        T.append((desc, x - 4, 702, col - 40, "small"))
    place(k, "viz-10", render("viz-10", P), T)


def s17():
    k = 17
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
    place(k, "viz-17", render("viz-17", P), T)


def s11():
    k = 11
    clear(k, "The fleet today")
    P, T = [], []
    cw, g = 400, 36
    xs = [104 + j * (cw + g) for j in range(4)]
    for j in range(30):
        P.append(icon("hard-drives", xs[0] + (j % 6) * 66, 392 + (j // 6) * 66, 42))
    for j in range(14):
        P.append(icon("user", xs[1] + (j % 5) * 80, 488 + (j // 5) * 80, 50))
    for j, name in enumerate(["nginx", "PHP-FPM", "MariaDB", "Valkey", "Security layers"]):
        y = 390 + j * 56
        P.append(rect(xs[2], y, cw, 44, PANEL, RULE, 2))
        T.append((name, xs[2] + 16, y + 5, cw - 32, "chip"))
    P.append(rect(xs[2], 674, cw, 44, VIOLET))
    T.append(("Linux", xs[2] + 16, 679, cw - 32, "chipw"))
    for j, (name, ic) in enumerate([("Analytics", "chart-line"), ("Docs", "files"), ("CRM", "address-book")]):
        box(P, T, xs[3], 390 + j * 112, cw, 92, ic, name, fill=TINT, stroke=VIOLET)
    cells = [("Dozens of clusters", "Self hosted Linux and virtualization."),
             ("14 people", "A web agency with its own sysop team."),
             ("Built for purpose", "Each server is set up for its use, with nothing extra installed."),
             ("Own your services", "Analytics, docs, CRM, and other software run on our own servers.")]
    for x, (label, body) in zip(xs, cells):
        T.append((label, x, 758, cw, "year"))
        T.append((body, x, 802, cw - 20, "small"))
    place(k, "viz-11", render("viz-11", P), T)


def s18():
    k = 18
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
        x0, y0 = hx + hw + 12, hy + hh // 2
        P.append(path(f"M{x0},{y0} C{x0 + 50},{y0} {x0 + 40},{cy} {x0 + 80},{cy} L1538,{cy}", VIOLET, 3))
    place(k, "viz-18", render("viz-18", P), T)


def s19():
    k = 19
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


def s12():
    k = 12
    clear(k, "From source and from upstream")
    P, T = [], []
    bh, sx, sw_ = 116, 1120, 692
    kw = dict(ls="label22", ds="desc20")
    rows = [(450, "file-code", "Module source", "Brotli, cache purging, GeoIP\u2026", 1),
            (600, "download-simple", "Upstream repositories", "nginx.org mainline, PPAs, MariaDB.", 1),
            (750, "package", "Distribution packages", "Everything else comes from\u2028the distribution.", 2)]
    for cy, ic, label, desc, nl in rows:
        box(P, T, 104, cy - bh // 2, 500, bh, ic, label, desc, nl, **kw)
    box(P, T, 680, 450 - bh // 2, 340, bh, "wrench", "Built here", "Against the running\u2028nginx version.", 2,
        fill=TINT, stroke=VIOLET, **kw)
    P.append(line(618, 450, 666, 450))
    P.append(line(1034, 450, sx - 14, 450))
    for cy in (600, 750):
        P.append(line(618, cy, sx - 14, cy))
    P.append(rect(sx, 392, sw_, 446, TINT, VIOLET, 2))
    P.append(icon("hard-drives", sx + 28, 420, 44))
    T.append(("Our server", sx + 94, 425, 400, "label22"))
    for j, chip in enumerate(["nginx and modules", "PHP", "MariaDB", "Distribution packages", "Applications", "FOSS"]):
        cx, cy2 = sx + 28 + (j % 2) * 326, 484 + (j // 2) * 64
        P.append(rect(cx, cy2, 310, 52, PANEL, RULE, 2))
        T.append((chip, cx + 20, cy2 + 10, 280, "chip"))
    P.append(rect(sx + 28, 684, 636, 126, VIOLET))
    T.append(("Our own configuration", sx + 48, 702, 600, "label22w"))
    T.append(("Every configuration file is ours,\u2028with our own defaults.", sx + 48, 736, 600, "desc20w"))
    place(k, "viz-12", render("viz-12", P), T)


def s14():
    k = 14
    clear(k, "Self-hosting needs standards too")
    P, T = [], []
    bh = 108
    for (cy, ic, label, desc), ty in zip([(460, "file-code", "Built from source", "Where the details matter."),
                                          (600, "list-checks", "Ansible playbooks", "The same setup on every server."),
                                          (740, "cube", "Docker", "For some services, where it fits.")], (560, 600, 640)):
        box(P, T, 104, cy - bh // 2, 500, bh, ic, label, desc)
        P.append(line(618, cy, 726, ty))
    box(P, T, 740, 515, 420, 170, "check-circle", "One standard", "Same rules for every\u2028kind of setup.", 2,
        fill=TINT, stroke=VIOLET)
    P.append(line(1174, 600, 1266, 600))
    box(P, T, 1280, 515, 532, 170, "book-open-text", "Written down", "Servers and code are both documented.", 2,
        fill=VIOLET, stroke=None, icol=PANEL, ls="nodew", ds="smallw")
    place(k, f"viz-{k}", render(f"viz-{k}", P), T)

# Code palette: one clearly different colour per token kind.
CODE = {"text": "#E4EAEC", "func": "#8FE3FF", "key": "#FF7EDB", "num": "#FFC9A3", "str": "#FFE0A3",
        "kw": "#A2FEE5", "punct": "#B8C2C7", "comment": "#A9B4BA"}


def code_lines(k, x, y, lines, size=26, step=40):
    """Each line is its own editable text item in Geist Mono; tokens are (text, kind)."""
    D = n.q(n.DOC)
    for j, toks in enumerate(lines):
        full = "".join(t for t, _ in toks)
        cmds = [f'''set t to make new text item with properties {{object text:{n.q(full)}, position:{{{x}, {y + j * step}}}, width:{len(full) * 16 + 40}}}
  tell object text of t
    set its font to "GeistMono-Regular"
    set its size to {size}
    set its color to {_rgb(CODE["text"])}
  end tell''']
        pos = 1
        for t, kind in toks:
            if t.strip() and kind != "text":
                cmds.append(f'set color of characters {pos} thru {pos + len(t) - 1} of object text of t to {_rgb(CODE[kind])}')
            pos += len(t)
        cmds.append(f"set position of t to {{{x}, {y + j * step}}}")
        n.osa(f'tell application "Keynote" to tell slide {k} of document {D}\n  ' + "\n  ".join(cmds) + "\nend tell")


def s13():
    k = 13
    d = n.dump(k)
    assert d[0]["text"] == "The package broke, source kept running", d[0]["text"]
    n.osa(f'''tell application "Keynote" to tell slide {k} of document {n.q(n.DOC)}
  repeat with i from (count of images) to 1 by -1
    set fn to file name of image i
    if fn starts with "code-" or fn starts with "viz-13" then delete image i
  end repeat
  repeat with i from (count of text items) to 1 by -1
    if font of object text of text item i is "GeistMono-Regular" then delete text item i
  end repeat
end tell''')
    P = [rect(108, 433, 819, 132, "#1B0B38"), rect(993, 433, 819, 252, "#1B0B38")]
    place(k, "viz-13", render("viz-13", P), [])
    left = [[("nginx", "func"), (" ", "text"), ("-v", "key")],
            [("nginx", "func"), (" ", "text"), ("-V", "key"), (" ", "text"), ("2", "num"), (">&", "punct"), ("1", "num"),
             (" ", "text"), ("|", "punct"), (" ", "text"), ("grep", "func"), (" ", "text"), ("configure", "str")]]
    right = [[("curl", "func"), (" ", "text"), ("-O", "key"), (" ", "text"), ("nginx.org/download/nginx-$V.tar.gz", "str")],
             [("tar", "func"), (" ", "text"), ("xzf", "key"), (" ", "text"), ("nginx-$V.tar.gz", "str"), (" ", "text"),
              ("&&", "punct"), (" ", "text"), ("cd", "kw"), (" ", "text"), ("nginx-$V", "str")],
             [("./configure", "func"), (" ", "text"), ("<same arguments>", "comment"), (" ", "text"), ("\\", "punct")],
             [("  ", "text"), ("--add-dynamic-module", "key"), ("=", "punct"), ("../ngx_cache_purge", "str")],
             [("make", "func"), (" ", "text"), ("modules", "kw")]]
    code_lines(k, 138, 452, left)
    code_lines(k, 1023, 452, right)
    n.osa(f'tell application "Keynote" to save document {n.q(n.DOC)}')

def s22():
    k = 22
    clear(k, "Where to start")
    P, T = [], []
    cols = [(104, "Start here", "New to running servers", [
                "Start on your own computer. Run one service, like\u2028a local AI model, and read its config files.",
                "Rent the smallest server and set it up yourself:\u2028SSH keys, firewall, nginx and TLS.",
                "Write every step down. Next month it is your script."]),
            (1008, "Go further", "Already running servers", [
                "Move one service you rent to your own server:\u2028analytics, docs or a status page.",
                "Swap one installed package for a source build.",
                "Test your exit. Restore a backup and move\u2028one service to another provider."])]
    num = 1
    for x, title, sub, tips in cols:
        T.append((title, x, 372, 800, "colhead"))
        T.append((sub, x, 432, 800, "colsub"))
        for j, tip in enumerate(tips):
            y = 520 + j * 124
            T.append((str(num), x, y + 3, 60, "tipnum"))
            T.append((tip, x + 64, y, 740, "tip30"))
            num += 1
    P.append(line(972, 380, 972, 860, RULE, 2, head=False))
    place(k, "viz-22", render("viz-22", P), T)

def s21():
    k = 21
    clear(k, "Big tech has alternatives")
    P, T = [], []
    T += [("Big tech", 104, 380, 440, "year"), ("European or self-hosted", 620, 380, 520, "year"), ("The catch", 1180, 380, 600, "year")]
    rows = [("Cloudflare", "Bunny.net, Slovenia", "Smaller network than Cloudflare."),
            ("Mailgun, SendGrid", "Brevo, France", "Delivery still depends on Gmail and Outlook."),
            ("GitHub", "Codeberg, Germany, or Forgejo", "Most open source projects still live on GitHub."),
            ("Google Workspace", "Nextcloud, self-hosted", "Someone has to run and update it."),
            ("OpenAI", "Mistral, France, or local models", "Local models need strong hardware.")]
    for j, (big, alt, catch) in enumerate(rows):
        y = 440 + j * 92
        P.append(rect(104, y, 440, 72, PANEL, RULE, 2))
        T.append((big, 128, y + (72 - lh("nodep")) // 2 - 2, 400, "nodep"))
        P.append(line(556, y + 36, 606, y + 36))
        P.append(rect(620, y, 520, 72, TINT, VIOLET, 2))
        T.append((alt, 644, y + (72 - lh("nodep")) // 2 - 2, 480, "nodep"))
        T.append((catch, 1180, y + (72 - lh("tip")) // 2 - 2, 640, "tip"))
    P.append(rect(1392, 214, 420, 104, PANEL, VIOLET, 2))
    T += [("More at", 1500, 232, 300, "small"), ("european-alternatives.eu", 1500, 262, 300, "chip")]
    place(k, "viz-21", render("viz-21", P), T)
    logo = os.path.abspath(os.path.join(HERE, "..", "keyassets", "brand", "ea-logo-no-text.svg"))
    n.osa(f'tell application "Keynote" to tell slide {k} of document {n.q(n.DOC)} to make new image with properties '
          f'{{file:(POSIX file {n.q(logo)}), position:{{1410, 230}}, width:72, height:72}}')
    n.osa(f'tell application "Keynote" to save document {n.q(n.DOC)}')


if __name__ == "__main__":
    for a in sys.argv[1:]:
        globals()["s" + a]()
