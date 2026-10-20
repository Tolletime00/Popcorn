# Books

The books you have finished, the ones you want to read, and recommendations, on an iPhone. Enter a title on the Finished tab or the Reading list tab, tap the book, and it lands on that shelf, grouped by year with the author and genre. Tap a book for its synopsis. The Recommend tab hands your request and both lists to Claude.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole app: screens, styles and logic in one file |
| `sw.js` | Lets the app open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The open-book icon |

- **Hosting:** GitHub Pages serves this folder from the `popcorn` repository, next to the Movies and Gym apps.
- **Book details and covers:** [Open Library](https://openlibrary.org), a project of the Internet Archive. No key or account is needed. Synopses come from Open Library, or from Google Books when Open Library has none.
- **Your lists:** stored on the phone, inside the Home Screen app. Nothing is sent anywhere else.
- **Backup:** the three dots on the Finished or Reading list tab, "Back up" saves `Books.csv` (Status, Title, Author, Year, Genre, Date, Open Library ID). Save it to OneDrive.

## Getting it back on a new phone

Nothing has to be rebuilt. The app is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/Popcorn/books/`.

1. Open the address in Safari on the new iPhone.
2. Tap Share, then Add to Home Screen. Keep "Open as Web App" on and tap Add.
3. Open Books from the Home Screen.
4. Tap the three dots, choose "Restore from a backup" and pick `Books.csv` from OneDrive.

Deleting the Books icon from the Home Screen deletes the lists stored in it. Back up first.

## Changing the app

Ask Claude for the change with the GitHub connection on; it commits the new `index.html` here. The app picks it up the next time it opens with a connection. Close the app fully and open it again if it looks unchanged.

## Credits

Book data from Open Library. The typeface is Jost, copyright 2020 The Jost Project Authors, used under the SIL Open Font License 1.1.
