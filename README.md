# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/taufan98/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/taufan98/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image summing up the world news of **Tuesday 24 November 2026**, built for the make.fun competition [news-image-20261124](https://make.fun/bounty/news-image-20261124) ("Sum up 24 November's world news in one image").

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## The image

A newspaper front page for **Tuesday 24 November 2026**, drawn from the day's reporting:

1. **Huang is back** — Nvidia reinstates Jensen Huang as CEO after an investigation; shares soar 31%.
2. **Warship sunk off Libya** — a Russian missile corvette is destroyed in an explosion and fire at Benghazi port.
3. **World Cup hosts picked** — FIFA names the hosts for the 2031 and 2035 Women's World Cups.
4. **Factory fire kills 30** — dozens dead or missing after a blaze at a sweet factory in Indonesia.
5. **O'Hare ground stop** — Chicago airport briefly halts flights amid the Thanksgiving travel rush.
6. **Denmark upholds 'ghetto law'** — the top court backs the hardline immigration housing law.

Also in the ticker: a Gaza toxic-contamination report, Lahore topping the world pollution ranking, and a supermoon meeting the Pleiades.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to `/output/entry.png`, checking the PNG magic bytes and the 1 MiB size cap first, then verifying the written copy by hash. No network; deterministic — every run writes the same bytes.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=va8excfs&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
