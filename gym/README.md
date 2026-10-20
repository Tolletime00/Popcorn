# Gym

A personal workout tracker for iPhone. Set up your routines (the exercises you do, one to five sets of each, and a rep target or range like 8 to 12), then work through one and record the weight and reps of every set. Each set has its own lb/kg switch, so kilogram plates and pound dumbbells can share a workout. Last time's numbers are filled in for you, so logging a set is one tap unless something changed.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole app: screens, styles and logic in one file |
| `sw.js` | Lets the app open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The dumbbell icon |

- **Hosting:** GitHub Pages serves this folder from the `popcorn` repository, next to the Movies app.
- **Routines and workouts:** stored on the phone, inside the Home Screen app. Nothing is sent anywhere.
- **Backup:** History, the three dots, "Back up" saves `Workouts.csv` (one row per set: date, time, routine, exercise, set, weight, reps, unit) and `Routines.csv` (routine, order, exercise, sets, reps or a range like 8-12). Save them to OneDrive.

## Getting it back on a new phone

Nothing has to be rebuilt. The app is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/popcorn/gym/`.

1. Open the address in Safari on the new iPhone.
2. Tap Share, then Add to Home Screen. Keep "Open as Web App" on and tap Add.
3. Open Gym from the Home Screen.
4. Go to History, tap the three dots, choose "Restore from a backup" and pick `Workouts.csv` and `Routines.csv` from OneDrive.

Deleting the Gym icon from the Home Screen deletes the routines and workouts stored in it. Back up first.

## Changing the app

Ask Claude for the change with the GitHub connection on; it commits the new `index.html` here. The app picks it up the next time it opens with a connection. Close the app fully and open it again if it looks unchanged.

## Credits

The typeface is Jost, copyright 2020 The Jost Project Authors, used under the SIL Open Font License 1.1.
