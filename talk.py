"""Mindtrek 2026: Sovereign by habit.

First draft, generated from the slide outline in the vault on 29.9.2026.
Values in [brackets] are facts still to be filled in. Once the deck is handed
over to Keynote, the .key becomes the source of truth and this file is kept
for reference only.
"""

EVENT = "Mindtrek 2026, Tampere, 6th of October, 2026"
RUNNING = "Sovereign by habit"

# head is the Unbounded part, em the Instrument Serif italic part.
DECK = [
    dict(layout="cover", head="Sovereign", em="by habit",
         standfirst=["20 years of self-hosting from source", "on European servers"]),

    dict(layout="statement", head="A strategy topic,", em="told from the server room",
         standfirst=["Europe is planning its way towards digital sovereignty.",
                     "This talk is about what it looks like in daily work."],
         notes="""The conference theme is Building Europe's Digital Sovereignty. Most of that conversation happens at the level of strategy and policy. This talk looks at the same thing from below: one small company, its servers, and the habits that keep them under its own control."""),

    dict(layout="pairs", head="The layers", em="we stopped looking inside", pairs=[
        ("Containers", "Package an application with everything it needs, so it runs the same everywhere."),
        ("Orchestration", "Schedule and scale those containers across many machines."),
        ("Managed platforms", "Someone else runs the servers, the database and the updates."),
        ("Headless and SaaS", "The content, the forms or the search live in another company's service."),
    ], notes="""Each of these solves a real problem, and I use some of them. What they have in common is that each one hides a layer that developers used to see. This talk is about what happens when you keep looking inside those layers."""),

    dict(layout="statement", head="Where the habit", em="comes from",
         standfirst=["[1998: the first machine and filesystem I could touch.]",
                     "About twenty years of Linux servers I can log into."],
         notes="""Code for 30 years, my own Linux servers for about two decades. The preference for servers I can log into came first. The word for it, sovereignty, came much later."""),

    dict(layout="bullets", head="2013:", em="a company on the same habit", items=[
        "Dude starts out on partners' hosting.",
        "Without root access, every change means waiting for someone else.",
        "[Year]: the first servers of our own.",
        "Since then, all of our infrastructure runs on European servers.",
    ], notes="""Drop this slide if the talk runs long. The point is that the company inherited the habit from the people who founded it."""),

    dict(layout="list", head="Choosing providers,", em="and leaving them", items=[
        "[Year] Partners' shared hosting",
        "[Year] The first VPS",
        "[Year] A French provider",
        "[Year] A Finnish datacentre",
        "[Year] The outage",
        "Today: a mix of European providers",
    ], notes="""Tell the outage as a story. It is the proof that leaving a provider is possible when you know every layer of your own setup. [What happened, when, and how long the move took.]"""),

    dict(layout="pairs", head="The fleet", em="today", pairs=[
        ("[N] servers", "[What each class of server runs.]"),
        ("15 people", "A web agency, no separate operations team."),
        ("Our own services", "Plausible for analytics, Outline for docs, Twenty for the CRM."),
        ("Mastodon", "mementomori.social, about 1000 users, since 2022."),
    ], notes="""One picture of what runs where. The self-hosted applications are evidence here, not a section of their own."""),

    dict(layout="pairs", head="From", em="upstream", pairs=[
        ("Built from source", "[Which software is compiled by hand.]"),
        ("Upstream packages", "[Which software comes from the distribution or upstream packages.]"),
        ("Configured by hand", "Every configuration file is written and read by us, with our own defaults."),
        ("Why the line is there", "[Why some things are built and others are packaged.]"),
    ], notes="""The title says "from source", so be exact. The distinction that holds up is upstream and unmodified software configured by hand, compared to a vendor image with somebody else's defaults already baked in. Say which packages and which builds before a question from the audience does."""),

    dict(layout="code", head="Working", em="on the server",
         left_label="Find it", left_code="ssh web-01\nless /etc/nginx/sites-enabled/example.conf\njournalctl -u nginx --since '10 min ago'",
         right_label="Fix it", right_code="sudo vim /etc/nginx/sites-enabled/example.conf\nsudo nginx -t\nsudo systemctl reload nginx",
         takeaway="Log in, read the configuration, change the thing, test it and reload. Every step is visible, and every step can be undone.",
         notes="""No live demo. [Replace these commands with one real sequence from our own servers.]"""),

    dict(layout="pairs", head="Automation,", em="and what stays manual", pairs=[
        ("Automated", "[Ansible playbooks, backups, monitoring, updates.]"),
        ("By hand", "[What we keep manual on purpose.]"),
        ("Coming round to it", "[How Ansible entered the picture.]"),
        ("The line between", "[How we decide which side something goes on.]"),
    ]),

    dict(layout="bullets", head="Where it", em="costs more", items=[
        "Onboarding takes longer when every layer is yours.",
        "Rebuilding a server exactly the same way needs discipline.",
        "Knowledge collects in one person unless it is written down.",
        "[Hours of maintenance per month, counted honestly.]",
    ], notes="""Be honest about the costs before talking about the benefits. [Monthly server cost compared to an equivalent managed platform.]"""),

    dict(layout="bullets", head="Where it", em="pays", items=[
        "Every layer is understood, so nothing is a black box.",
        "Problems can be read from logs and configuration files.",
        "Moving to another provider is work, but it is possible.",
        "[The debugging story where reading the layer solved it.]",
    ]),

    dict(layout="pairs", head="Where it", em="still leaks", pairs=[
        ("DNS", "[Who runs our DNS, and what happens if they go away.]"),
        ("CDN", "[Where static files and caching depend on another company.]"),
        ("Email", "Deliverability depends on the large mail providers."),
        ("AI APIs", "The models we use run on servers we do not control."),
    ], notes="""Self-hosting does not make a company fully independent. These are the dependencies we keep, and knowing them is part of the work. This ties back to the strategy view on the second slide."""),

    dict(layout="statement", head="Knowing every layer", em="is practical sovereignty",
         standfirst=["Host one thing yourself, end to end,", "and keep it running for a year."],
         notes="""One concrete first step for the developers and students in the room."""),

    dict(layout="statement", head="Kiitos.", em="Questions?",
         standfirst=["Rolle Laukkarinen", "rolle.social · dude.fi · github.com/rollecode"]),
]

LOGO = ("mindtrek-logo.svg", "mindtrek.png", 47, "Mindtrek")
VENUE = "Developers track, Finnkino Cine Atlas, Tampere"
SLOT_MIN = 30
QA_MIN = 10
KEY_NAME = "Sovereign by habit"

NOTES = """
## Before the stage

- Slides go to presentations@mindtrek.org as PowerPoint or PDF by Sunday 4.10
- The talk is 20 minutes, with 5 to 10 minutes for questions
- Fill in every [bracket] with the real value, or remove the line
"""
