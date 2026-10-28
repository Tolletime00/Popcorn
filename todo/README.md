# To-Do

A planner for iPhone with five tabs. **Calendar** lists the coming days, each with its yearly dates first, then that day's weekly and monthly items in grey italics, then the items put on that day; tap the circle to tick something off and it goes (tap again within a second if it was a slip); drag an item by the two lines at its end, or hold it anywhere, to move it to another day or another spot. Weekly and monthly items move on the Calendar too: within the day, or to another day for that one time, while their own tabs keep the pattern. Every weekday carries two dividers, "Drive to work" and "Drive home from work": not items, just lines to put things above and below; drag them within a day; tap one to rename it, take it off just that day (a holiday, say), delete it from that weekday, or delete it from every day; and add more from the Weekly tab. **Weekly** is the week, Monday to Sunday, for things that repeat every week. **Monthly** is the 1st to the 31st, for things that repeat every month (the 31st falls on the last day of shorter months). **List** is anything else, in any order, with sections if you want them; an item can be put on the Calendar from its page. **Special** is the dates that come round every year, birthdays and holidays, starting with the days the stock market is closed. Every item can be marked personal (blue) or work (green).

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole app: screens, styles and logic in one file |
| `sw.js` | Lets the app open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The check-mark icon |

- **Hosting:** GitHub Pages serves this folder from the `popcorn` repository, next to the Movies, Gym and Books apps.
- **Your items:** stored on the phone, inside the Home Screen app. Nothing is sent anywhere.
- **Backup:** the three dots on any tab, "Back up" saves `To-Do backup.json`, one file with everything in it. Save it to OneDrive. "Restore from a backup" replaces what is in the app with that file.
- **Market holidays:** New Year's Day, Martin Luther King Jr. Day, Presidents' Day, Good Friday, Memorial Day, Juneteenth, Independence Day, Labor Day, Thanksgiving and Christmas, worked out for each year by their rules. A holiday that lands on a weekend also shows the weekday the market closes instead.

## Getting it back on a new phone

Nothing has to be rebuilt. The app is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/Popcorn/todo/`.

1. Open the address in Safari on the new iPhone.
2. Tap Share, then Add to Home Screen. Keep "Open as Web App" on and tap Add.
3. Open To-Do from the Home Screen.
4. Tap the three dots, choose "Restore from a backup" and pick `To-Do backup.json` from OneDrive.

Deleting the To-Do icon from the Home Screen deletes everything stored in it. Back up first.

## Changing the app

Ask Claude for the change with the GitHub connection on; it commits the new `index.html` here. The app picks it up the next time it opens with a connection. Close the app fully and open it again if it looks unchanged.

## Credits

The typeface is Jost, copyright 2020 The Jost Project Authors, used under the SIL Open Font License 1.1.
