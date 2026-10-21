# Bubbles

Bubbles float up; you pop them. For small kids: no losing, no timer, nothing to read.

- Tap a bubble to pop it, or drag a finger through a few. Several fingers at once all work.
- The number at the top counts the pops. Every 25, a little party of confetti and a tune, and the game just carries on.
- Now and then a golden star bubble comes up; popping it plays a jingle.
- Bubbles that reach the top simply float away.
- The start screen has Few / Lots (how many bubbles at once), which the app remembers, and a sound switch. The house button in the corner goes back to the start.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for. Nothing is stored except those two settings.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole game: the bubbles, the sounds and the logic in one file |
| `sw.js` | Lets the game open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The bubbles icon |

## Putting it on an iPad

The game is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/Popcorn/bubbles/`.

1. Open the address in Safari.
2. Tap Share, then Add to Home Screen, then Add.
3. Open Bubbles from the Home Screen; it fills the whole screen with no Safari bars.
