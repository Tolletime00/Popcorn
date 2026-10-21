# Bounce

A two-player paddle game for small kids. Blue is on the left, Orange on the right; first to five wins.

- **On an iPad or iPhone:** each player holds their own two buttons, blue on the left and orange on the right. Up is the top one.
- **On a keyboard:** Blue uses `Q` (up) and `A` (down); Orange uses the `↑` and `↓` arrow keys. Space pauses.
- The ball starts slow and gets a little quicker during a rally, then resets after each point. The start screen has a Slow / Normal / Fast choice, which the app remembers, and a sound switch.
- Tap Play (or press any key, or any of the four buttons) to start. After a win, the screen waits a couple of seconds before a button press starts a new game, so nobody skips the confetti.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for. Nothing is stored except the speed and sound settings.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole game: the court, the buttons, the sounds and the logic in one file |
| `sw.js` | Lets the game open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The paddles-and-ball icon |

## Putting it on an iPad

The game is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/Popcorn/bounce/`.

1. Open the address in Safari.
2. Tap Share, then Add to Home Screen, then Add.
3. Open Bounce from the Home Screen; it fills the whole screen with no Safari bars.
