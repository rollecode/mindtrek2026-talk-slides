"""Mindtrek 2026: Sovereign by habit.

First draft, generated from the slide outline in the vault on 29.9.2026.
Facts come from the submitted abstract, the Dude blog posts of 2017 and 2023 and the server install scripts. Once the deck is handed
over to Keynote, the .key becomes the source of truth and this file is kept
for reference only.
"""

EVENT = "Mindtrek 2026, Tampere, 6th of October, 2026"
RUNNING = "Sovereign by habit"

# head is the Unbounded part, em the Instrument Serif italic part.
DECK = [
    dict(layout="cover", head="Sovereign", em="by habit",
         standfirst=["20 years of self-hosting from source", "on European servers"]),

    # Same as the WP Suomi 2026 about slide, text taken from its final export.
    dict(layout="about", sections=[
        ("About", "Rolle", "Founder and CTO of Digitoimisto Dude Oy. Code soon 30 years, WordPress since 2005, online since 1999. Accessibility, open source, Linux servers, and building my own tools. Free time: running, bilingual family, knows sign language."),
        ("Dude &", "WordPress", "Contributing to WordPress and open source since we founded Dude in 2013: 71 open source repositories on GitHub, including air-light, our starter theme with over 1100 stars."),
    ], photos=["photos/rolle-90s.jpg", "photos/dudella.jpg"]),

    dict(layout="statement", head="Sovereignty as a strategy,", em="or as a habit",
         standfirst=["Europe's digital sovereignty has become a strategy topic,",
                     "something organisations plan their way towards.",
                     "This talk is about getting there by habit."],
         notes="""The conference theme is Building Europe's Digital Sovereignty. This talk looks at it from the daily work of one small agency and its servers."""),

    dict(layout="pairs", head="Layers we rarely", em="look inside", pairs=[
        ("Containers", "An image bundles the app with an operating system someone else chose."),
        ("Orchestration", "A scheduler decides where and when the containers run."),
        ("Managed platforms", "No shell and no filesystem. You deploy, the platform runs it."),
        ("Serverless", "Functions run on demand in another company's runtime."),
    ], notes="""These layers solve real problems, and I use some of them. For 20 years my preference has been different: build from source, and run things on servers I can log into, read and change."""),

    dict(layout="pairs", head="Where the habit", em="comes from", pairs=[
        ("1996", "KDE at 8 years old, on the family's Red Hat based Linux."),
        ("1998", "Mandrake Linux, dual-booted on my sister's PC."),
        ("School", "An IRC shell account on TNNet."),
        ("Later", "A headless server in the wardrobe, used over SSH."),
    ], notes="""My father had an Amstrad CPC, then 386 and 486 machines. Linux was in the house early, and a server I could log into became normal long before I had a word for why it mattered. [Check: the year of the first own server, which the "20 years" in the title rests on.]"""),

    dict(layout="bullets", head="Dude 2013-2015:", em="from partners to our own server", items=[
        "2013: client sites on hosting partners' servers.",
        "Jails, cPanel and control panels stood between us and the server.",
        "2015: our first own VPS, to run the latest nginx.",
        "Apache out, nginx in, for good.",
    ], notes="""I wanted a purely command-line way of working. The first VPS ran HHVM, which kept crashing, so I wrote a cron script that restarted it. That was the start of doing operations ourselves."""),

    dict(layout="list", head="Choosing providers,", em="and leaving them", items=[
        "2015  DigitalOcean: the first VPS",
        "2016  OVH in France: 2 web, 2 database and 1 file server",
        "2016  The outage: every client site hangs",
        "2016  Every site moved to Multim in Pori in one night",
        "2016-2026  A datacentre in a former army rock cave, on wind power",
        "2026  Moving everything to one Finnish provider",
    ], notes="""One Monday morning every client site hung, and nobody in France could be reached. Weeks later a report arrived: an excavator had cut the network. We moved every site to Multim in one night in October 2016. The old DigitalOcean server we kept for legacy sites is still called Monday. [Check: the 2016 blog post describes weeks of slow nights before the move; settle which version to tell.]"""),

    dict(layout="pairs", head="The fleet", em="today", pairs=[
        ("About 30 servers", "Ubuntu 24.04 on almost all of them."),
        ("15 people", "A web agency with no separate operations team."),
        ("One stack per server", "nginx, PHP-FPM, MariaDB, Valkey and fail2ban on the same machine."),
        ("Our own services", "Analytics, docs, CRM and a Mastodon instance with 1000 users."),
    ], notes="""Deploys go from Git with Capistrano. Larger sites get a cluster with HAProxy, Galera and lsyncd. The self-hosted services are Plausible, Outline, Twenty and mementomori.social."""),

    dict(layout="pairs", head="From source", em="and from upstream", pairs=[
        ("Built from source", "nginx modules for Brotli, cache purging and GeoIP, against the exact nginx that runs."),
        ("Upstream repositories", "nginx from nginx.org, PHP from the Ondřej Surý PPA, MariaDB from MariaDB."),
        ("Distribution packages", "Everything else comes from Ubuntu."),
        ("Configured by hand", "Every configuration file is ours, with our own defaults."),
    ], notes="""The title says from source, so to be exact: most software comes from upstream, and a few modules are compiled by us. What matters is unmodified upstream software, configured by hand, on a server we can read."""),

    dict(layout="code", head="When a layer", em="breaks",
         left_label="Read the running build", left_code="nginx -V 2>&1 | grep configure\napt-get source nginx",
         right_label="Build the module against it", right_code="cd nginx-*/\n./configure <same arguments> \\\n  --add-dynamic-module=../ngx_cache_purge\nmake modules",
         takeaway="Ubuntu patched nginx for a security fix, and our modules built from plain nginx source started crashing. Building them against Ubuntu's own source, with the same configure arguments, fixed it.",
         notes="""This is the whole talk in one incident. The crash was a segfault inside a module. Knowing how nginx and its modules are built is what found the cause."""),

    dict(layout="pairs", head="Automation,", em="and what stays manual", pairs=[
        ("Scripts", "Bash install and maintenance scripts since 2025, now moving to Ansible."),
        ("Every hour", "Database and file backups to a storage box, with daily and weekly snapshots."),
        ("Monitoring", "Logs, errors and suspicious requests are watched and reported to Slack."),
        ("By hand", "Monthly patching follows a written runbook and takes about 3 hours."),
    ], notes="""Ansible is something I used to do only with a gun to my head. Lately I have grown fond of it."""),

    dict(layout="bullets", head="Where it", em="costs more", items=[
        "Monthly patching takes hours, and only two people can do it.",
        "Servers set up at different times drift apart.",
        "Fixes are made by hand first and written into scripts afterwards.",
        "Knowledge stays with a few people unless it is written down.",
    ]),

    dict(layout="bullets", head="Where it", em="pays", items=[
        "Every layer can be read, so nothing is a black box.",
        "A crash can be traced from the log to the source.",
        "In 2016 we moved every site to another provider in one night.",
        "The 2026 move to one provider is planned in waves over three months.",
    ]),

    dict(layout="pairs", head="Where it still", em="depends on others", pairs=[
        ("DNS and CDN", "Cloudflare, for DNS, caching and the Mastodon media storage."),
        ("Email", "Mailgun sends it, and delivery depends on the large mail providers."),
        ("Code and tools", "GitHub for code, Better Stack for uptime, Let's Encrypt for certificates."),
        ("AI", "Log analysis uses OpenAI models, and I use Claude a lot."),
    ], notes="""Self-hosting does not make a company independent of everyone. These are the dependencies we keep on purpose, and knowing them is part of the work."""),

    dict(layout="statement", head="Knowing every layer", em="is practical sovereignty",
         standfirst=["Host one thing yourself, end to end,", "and keep it running for a year."],
         notes="""Knowing every layer of your stack is the most practical form of digital sovereignty a developer can have. One concrete first step for the developers and students in the room."""),

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
- Settle the two [Check] notes: the year of the first own server, and which outage version to tell
"""
