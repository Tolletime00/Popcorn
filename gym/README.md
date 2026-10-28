# Gym

A personal workout tracker for an iPad or an iPhone. On an iPad the three sections sit in a sidebar and stay put while you train; on an iPhone they are the tabs along the bottom. Same app, same address, same backup files. Set up your routines (the exercises you do, one to five sets of each, and a rep target or range like 8 to 12), then work through one and record the weight and reps of every set. Each set has its own lb / kg / bodyweight switch, so kilogram plates, pound dumbbells and pull-ups can share a workout. An exercise can track time instead of reps (the exercise's three dots, "Track time instead of reps"): a run or a row records minutes and seconds for each set. Two exercises in a row can be paired as a superset (the same menu, "Superset with …"); a workout then lists them as alternating A and B sets. Last time's numbers are filled in for you, so logging a set is one tap unless something changed. Logging a set starts the rest timer in the top corner, which counts up until the next set is logged. The Workout screen lists the routines with the one that has waited longest first, until you drag them (by the two lines at the end of a row, or by holding one) into an order of your own; that order then holds, with new routines at the end.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole app: screens, styles and logic in one file |
| `sw.js` | Lets the app open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The dumbbell icon |

- **Hosting:** GitHub Pages serves this folder from the `popcorn` repository, next to the Movies app.
- **Routines and workouts:** stored on the device, inside the Home Screen app. Nothing is sent anywhere. An iPhone and an iPad each keep their own copy; the backup is how they move between them.
- **Backup:** History, the three dots, "Back up" saves `Workouts.csv` (one row per set: date, time, routine, exercise, set, weight, reps, unit — "bodyweight" when there was none — and the duration of a timed set as m:ss) and `Routines.csv` (routine, order, exercise, sets, reps or a range like 8-12, "with next" in the Superset column for the first exercise of a pair, and a Type of "weight" or "time"). Save them to OneDrive.

## Moving it to an iPad (or a new iPhone)

Nothing has to be rebuilt. The app is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/popcorn/gym/`.

1. On the iPhone: History, the three dots, Back up, and save `Workouts.csv` and `Routines.csv` to OneDrive.
2. On the iPad: open the address in Safari, tap Share, then Add to Home Screen. Keep "Open as Web App" on and tap Add.
3. Open Gym from the Home Screen. The Workout screen offers "Restore from a backup": tap it and pick both spreadsheets from OneDrive (one at a time is fine too). Later on, the same thing is under History's three dots.

Restoring adds what is new and leaves what is already there, so it is safe to do more than once. Deleting the Gym icon from the Home Screen deletes the routines and workouts stored in it. Back up first.

## Changing the app

Ask Claude for the change with the GitHub connection on; it commits the new `index.html` here. The app picks it up the next time it opens with a connection. Close the app fully and open it again if it looks unchanged.

## Credits

The typeface is Jost, copyright 2020 The Jost Project Authors, used under the SIL Open Font License 1.1.
