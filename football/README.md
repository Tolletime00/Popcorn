# Football

NFL bets, power rankings and matchups, on an iPhone.

- **Bets:** each bet is a week, a team, a spread and odds, sized to win $100. It settles itself from the final score (win, loss or push) and the season's P/L and record sit at the top right.
- **Power Rankings:** every team in a tier from +7 to −10 (points better or worse than average), dragged into place, with its record, one number for the team as a whole, and six for its sides: offense and defense, overall, pass and rush. The first number is the team's rank of the 32 by the average of its offense and defense (the defense counted the right way round, so a stingy defense helps); the six are its rank of the 32 for that stat — by EPA per play or by the DVOA-style rating, whichever the switch shows — 1 for the best offense or the stingiest defense, 32 for the worst, coloured green for 1 through grey to red for 32. The team screen has the figures behind the ranks. Tap a team for its game log, coloured by margin, with each opponent's rating beside its name; the team screen shows both sets, with each DVOA-style number's rank among the 32.
- **Matchups:** the coming week's games in order, with the spread, the line your own ratings imply (home rating − away rating + 1.5 for home field), a rest line when it matters (off a bye, played Thursday or Monday, played overseas, a short week for both), and each offense's rank of the 32 against the rank of the defense it faces — overall, pass and rush, by EPA or DVOA-style on the same switch, tinted by the gap between the two ranks. Games abroad name their city. Tap either team for its game log.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for.

## Where the numbers come from

`update.py` runs on GitHub's computers every half hour (the `Football data` workflow in `.github/workflows`) and rewrites `data/data.json`:

- **Schedule, spreads, scores, rest days and venues:** [nflverse](https://github.com/nflverse/nflverse-data) `games.csv` (its `away_rest`/`home_rest` are the days since each team last played; overseas stadiums are recognised by name), with ESPN's public scoreboard laid over it for live scores, final status and the latest spreads.
- **EPA:** nflverse play-by-play for the season, the same data rbsdm.com is built on. Regular season, pass and rush plays with an EPA value; offense by the team with the ball, defense by the team without it.
- **DVOA-style** (`dvoa_calc.py`): our own calculation from the same play-by-play, built the way FTN describes DVOA — success points per play (45% / 60% / 100% of the needed yards on 1st / 2nd / 3rd-and-4th down, bonuses for big plays, penalties for losses and turnovers), compared with the league average for the situation, then adjusted for the opponent. Offense, defense, and the pass and rush splits, as percentages: offense higher is better, defense lower. It is **not** FTN's DVOA — their exact tables aren't public — but on the 2024 and 2025 seasons it landed within about three points of their published offense and defense numbers for the typical team (correlation 0.97 offense, 0.92–0.95 defense). No special teams.
- **Logos:** ESPN, fetched once into `logos/`.

The app refreshes that file when it opens and when you tap Refresh. Bets and rankings never leave the phone; the three dots back them up to one file for OneDrive and restore from it.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole app: screens, styles and logic in one file |
| `sw.js` | Lets the app open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The football icon |
| `update.py` | Rebuilds `data/data.json` and fetches the logos |
| `dvoa_calc.py` | The DVOA-style calculation `update.py` runs |
| `data/data.json` | Games, scores, spreads, EPA and DVOA-style ratings for the season |
| `logos/` | One PNG per team |

## Getting it back on a new phone

Nothing has to be rebuilt. The app is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/Popcorn/football/`.

1. Open the address in Safari on the new iPhone.
2. Tap Share, then Add to Home Screen. Keep "Open as Web App" on and tap Add.
3. Open Football from the Home Screen.
4. Tap the three dots, choose "Restore from a backup" and pick `Football backup.json` from OneDrive.

## Changing the app

Ask Claude for the change with the GitHub connection on; it commits the new `index.html` here. The app picks it up the next time it opens with a connection.

## Credits

Data from nflverse and ESPN. The typeface is Jost, copyright 2020 The Jost Project Authors, used under the SIL Open Font License 1.1.
