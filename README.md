<h1 align="center">Sovereign by habit</h1>

<p align="center">
  <strong>20 years of self-hosting from source on European servers. A talk for Mindtrek 2026.</strong>
</p>

---

> [!IMPORTANT]
> These slides are a work in progress and subject to change until the talk has been given.

## The talk

| | |
| -- | -- |
| Event | [Mindtrek 2026](https://www.mindtrek.org/2026/program/), Finnkino Cine Atlas, Tampere |
| Slot | Tuesday 6.10.2026, 11:45-12:15, Developers track, 20 minutes plus Q&A |
| Audience | Developers working with open source, and students |

Europe's digital sovereignty is usually talked about as a strategy. The talk looks at it from the daily work of one small agency: servers run from source and from upstream, the work involved, the benefits, and how to start.

## Where to start

The tips from the talk, in a little more detail.

**Start here**

1. **Start on your own computer.** Run one service locally, like a local AI model, your notes or your development environment, and read its configuration files, not just the docs.
2. **Rent the smallest server and set it up yourself once.** SSH keys, a firewall, nginx and TLS. Lock yourself out on purpose and get back in through the provider's console.
3. **Write every step down.** Next month the list becomes your script.

**Go further**

4. **Move one service you rent to your own server.** Analytics, docs or a status page are good first candidates.
5. **Swap one installed package for a source build,** and learn its build options.
6. **Test your exit.** Restore a backup, and move one service to another provider. If it takes weeks, you are locked in.

## Reading

| | |
| -- | -- |
| [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) | A long, maintained list of software you can host yourself |
| [nginx downloads](https://nginx.org/en/download.html) | Mainline and stable source releases |
| [Building nginx from sources](https://nginx.org/en/docs/configure.html) | The configure options, including dynamic modules |
| [USN-8398-1](https://ubuntu.com/security/notices/USN-8398-1) and [USN-8398-2](https://ubuntu.com/security/notices/USN-8398-2) | The June 2026 Ubuntu nginx update, its crash with external modules, and the revert |
| [Duden harharetki palvelinmaailmassa](https://www.dude.fi/harharetki-palvelinmaailmassa) | The 2016 outage and the move to Finland, in Finnish |
| [Dude 10 vuotta, osa 2: Palvelimet](https://www.dude.fi/dude-10-vuotta-osa-2-palvelimet) | The history of Dude's servers, in Finnish |
| [air-light](https://github.com/digitoimistodude/air-light) | Dude's open source WordPress starter theme |

## Structure

| Path | What it is |
| -- | -- |
| `Sovereign by habit.key` | The deck used for presenting, and the source of truth |
| `keyassets/` | Logos, diagram parts and brand assets used on the slides |
| `photos/` | Photos used on the About slide |
| `tools/` | Helpers for editing the open deck in Keynote: diagrams, the logo wall and text |
| `talk.py` | Talk length settings used by the timing bar script |
| `minutes.json` | Estimated minutes per slide, used by the footer timing bars |

## Working on the deck

The first version of the deck was generated with [keynote-base](https://github.com/rollecode/keynote-base). Since then it has been edited in Keynote, and it is not generated again. Diagrams are rebuilt with `tools/visuals.py`, where every box, arrow and icon is its own object and every label is editable text.
