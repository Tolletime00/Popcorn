# Movies

This repository also holds five more apps: **Gym** in the `gym` folder, **Books** in the `books` folder, **To-Do** in the `todo` folder, **Football** in the `football` folder and **Budget** in the `budget` folder. Each has its own notes (`gym/README.md`, `books/README.md`, `todo/README.md`, `football/README.md`, `budget/README.md`), and each one's address is the Movies address with `gym/`, `books/`, `todo/`, `football/` or `budget/` on the end. Football's scores, spreads and EPA are rebuilt every half hour by the `Football data` workflow in `.github/workflows`.

A personal movie-rating app for iPhone. Rate the movie you just watched on a 1 to 5 scale (Bad, Meh, Good, Great, Perfect), keep a searchable log (grouped by rating, newest year first, with any rating level hideable), keep a watchlist of movies to see (newest year first, with genres and a synopsis), and ask Claude for recommendations based on what you have and haven't seen.

It is a web app that lives on the Home Screen. There is no App Store, no Mac and nothing to pay for.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole app: screens, styles and logic in one file |
| `sw.js` | Lets the app open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The popcorn icon |

- **Hosting:** GitHub Pages serves these files from this repository for free.
- **Movie data and posters:** [TMDB](https://www.themoviedb.org). Each phone uses its owner's free TMDB API key, pasted into the app once. The key is stored on the phone, never in this repository.
- **Ratings and watchlist:** stored on the phone, inside the Home Screen app. They are not in this repository and never leave the phone except in the backup you save.
- **Backup:** Log, the three dots, "Back up" saves `Movie Ratings.csv` (Title, Year, Rating 1-5, Date Rated, TMDB ID) and, if you have one, `Watchlist.csv` (Title, Year, Date Added, TMDB ID). Save them to OneDrive.
- **Recommendations:** the Recommend tab hands your request and your ratings to the Claude app.

## Getting it back on a new phone

Nothing has to be rebuilt. The app is this repository's GitHub Pages address.

1. Open the address in Safari on the new iPhone. It looks like `https://YOUR-USERNAME.github.io/popcorn/`.
2. Tap Share, then Add to Home Screen. Keep "Open as Web App" on and tap Add.
3. Open Movies from the Home Screen.
4. Paste your TMDB key. It is on themoviedb.org under Settings, then API (the one called API Key).
5. Go to Log, tap the three dots, choose "Restore from a backup" and pick `Movie Ratings.csv` and `Watchlist.csv` from OneDrive.

Two things to know:

- Deleting the Movies icon from the Home Screen deletes the ratings stored in it. Back up first.
- Ratings added in Safari and ratings added in the Home Screen app are kept separately. Always use the Home Screen app.

## Changing the app

Ask Claude for the change and give it `index.html` from this repository. Upload the new `index.html` here (Add file, Upload files, Commit changes). The app picks it up the next time it opens with a connection, usually within ten minutes. Close the app fully and open it again if it looks unchanged.

Earlier versions of the app used a 1 to 10 scale. This version converts those ratings on its own, both the ones already on the phone and the ones in an old backup file (1-2 become 1, 3-4 become 2, 5-6 become 3, 7-8 become 4, 9-10 become 5).

## Credits

This product uses the TMDB API but is not endorsed or certified by TMDB. TMDB's API is free for non-commercial use.

The typeface is Jost, copyright 2020 The Jost Project Authors, used under the SIL Open Font License 1.1.
