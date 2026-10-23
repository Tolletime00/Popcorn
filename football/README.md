# Football

NFL bets, power rankings and matchups, on an iPhone.

- **Bets:** each bet is a week, a team, a spread and odds, sized to win $100. It settles itself from the final score (win, loss or push) and the season's P/L and record sit at the top right.
- **Power Rankings:** every team in a tier from +7 to −10 (points better or worse than average), dragged into place, with its record and six EPA numbers: offense and defense, EPA per play, per dropback and per rush. Tap a team for its game log, coloured by margin, with each opponent's rating beside its name.
- **Matchups:** the coming week's games in order, with the spread, the line your own ratings imply (home rating − away rating + 1.5 for home field), and each offense scored against the other defense: EPA per play, pass and rush. Tap either team for its game log.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for.

## Where the numbers come from

`update.py` runs on GitHub's computers every half hour (the `Football data` workflow in `.github/workflows`) and rewrites `data/data.json`:

- **Schedule, spreads and scores:** [nflverse](https://github.com/nflverse/nflverse-data) `games.csv`, with ESPN's public scoreboard laid over it for live scores, final status and the latest spreads.
- **EPA:** nflverse play-by-play for the season, the same data rbsdm.com is built on. Regular season, pass and rush plays with an EPA value; offense by the team with the ball, defense by the team without it.
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
| `data/data.json` | Games, scores, spreads and EPA for the season |
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
