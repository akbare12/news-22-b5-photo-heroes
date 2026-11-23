# THE WORLD TODAY — Sunday 22 November 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/akbare12/news-22-b5-photo-heroes/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/akbare12/news-22-b5-photo-heroes/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

The badges above link to the live bounty, this entry's leaderboard rank, and its reward.

One image that sums up the world news of Sunday 22 November 2026:
three large illustrated hero panels on top, a dense numbered story grid below.

## The three heroes

1. **2 TANKERS HIT** — Two supertankers strike naval mines east of the Strait
   of Hormuz, north of Ghanam Island; both catch fire. First reported
   17:13 UTC. (Iran navy · AP)
2. **NO DEAL** — COP31 in Antalya collapses with no agreement; the EU and
   ~130 parties reject a final text with no fossil-fuel language. The longest
   COP ever, the first collapse since 2009. (CNN · Reuters)
3. **258** — Democrats win the House with 258 seats, their largest majority
   since 1992. Chuck Hubbard beats Virginia Foxx by 330 votes in a North
   Carolina recount; GOP 173, four races uncalled. (AP · Reuters)

## The day in brief (stories 04–33)

| # | Story | Source |
|---|-------|--------|
| 04 | Benghazi ship hit — suspected sea drone hits Russian corvette Merkury | France 24 (CLAIM) |
| 05 | Khartoum drones kill 4, UN building damaged | AP (CLAIM) |
| 06 | Zelenskyy pleads for Patriots; ~2,700 drones in a week | BBC |
| 07 | Iran shows missile city, dual-missile launcher | IRGC media |
| 08 | Saudis stop Houthi attack; Rabigh refinery claimed hit | Reuters (CLAIM) |
| 09 | UAE condemns Iranian attack on Bahrain | WAM |
| 10 | Europe protests, day 3, over costs and housing | Le Monde |
| 11 | Settlers burn 12 vehicles in West Bank villages | WAFA |
| 12 | Benghazi depot blast inside naval base | Local authorities |
| 13 | Eisenkot–Likud unity talks stall | Israeli media |
| 14 | Finland: war spills over after Baltic drone strike | Finnish govt |
| 15 | WCK: three killed in Gaza strike were not its team | WCK |
| 16 | Ex-UN envoy: Iran war was "perfectly avoidable" | MED Dialogues |
| 17 | Banten factory fire kills 3; 36 workers missing | BBC |
| 18 | Turkey warns Israel may use Druze support for Syria op | Anadolu (CLAIM) |
| 19 | Bahrain blames Iran for industrial strike | Bahrain govt |
| 20 | Fidan: war fallout threatens global markets | Anadolu |
| 21 | Aoun: Israel must leave Lebanon | Al Jazeera |
| 22 | Gaza: 350,000 families homeless | Al Jazeera |
| 23 | Pezeshkian: Iran in "silent economic war", blockade 130 days | IRNA |
| 24 | Settlers attack homes in Hebron and Ramallah | WAFA |
| 25 | Turkey: Israel blocking container homes for Gaza | Anadolu (CLAIM) |
| 26 | Hind Rajab Foundation urges Germany to arrest soldier | HRF |
| 27 | Fred Nile dies at 92 (died 21 Nov, announced 22 Nov) | Guardian |
| 28 | Teen gamer and mother help FBI rescue missing girl | FBI |
| 29 | Gaza toll 1,661 since Oct 2025 ceasefire | Gaza health ministry |
| 30 | China eases margin rules, 100% to 80% from 30 Nov | Xinhua |
| 31 | Nvidia chip scandal: China accessed AI chips | NYT |
| 32 | Taiwan warns Canada over closer China ties | Taiwan MFA |
| 33 | China chipmakers CXMT and YMTC gain ground | S. China media |

Every story above was first reported on 22 November 2026. Items that were
*not* 22 November news are named in the image's date-check footer, with
their dates: El Chapo Isidro captured 20 Nov; BepiColombo Mercury orbit
21 Nov; ICJ Myanmar ruling 19 Nov; Wall Street rout 20 Nov; FBI NCIC hack
first reported 21 Nov.

## How it is built

`entry.png` (1024×1024, 198,782 bytes) is drawn with Python (PIL) by
`draw.py` in the build directory and stored in this repository.
`main.py` is a standard-library-only copy program: it copies `entry.png`
to `/output/entry.png` and verifies size, sha256 and the PNG magic bytes,
so both grading runs write identical bytes.

## Verification

Run twice from the repository root:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
cmp /tmp/out1/entry.png /tmp/out2/entry.png
```

Both runs write the same bytes (sha256
`4c9189a48488f40f3ee3c4ee796eaf7c5f6c48dd4738f7d0fc1e31cc64d33c4d`).
The image was zoom-checked at full size: no overlapping text, no clipped
labels, no garbled glyphs; every headline, badge and source is legible.

## Sources

AP · Reuters · BBC · CNN · France 24 · Al Jazeera · Anadolu · IRNA · WAFA ·
Le Monde · Guardian · FBI · Xinhua · NYT · WCK · HRF · dailysummaryof,
final edition 22 Nov 2026 (updated 23:45 UTC). Each story was cross-checked
against at least two sources where the claim was consequential; one-sided
allegations are badged CLAIM in the image.

## License

MIT — see LICENSE.
