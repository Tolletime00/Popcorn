# Numbers

A tapping game with numbers for small kids. Ten stars wins.

- **Find it:** a number is shown big at the top and said out loud ("Find seven"). Tap the balloon with that number on it. The right one pops and a star lights up; a wrong one just wobbles and the number is said again.
- **How many:** some animals or things appear. Count them and tap the right number underneath.
- **Numbers up to 5 or 10:** chosen on the start screen and remembered. 5 is the gentle setting.
- Tap the number card at the top to hear it again. On a keyboard, typing the number works too.
- The house button in the corner goes back to the start screen.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for. The only things stored are the game, range and sound settings. The voice is the iPad's own; it may stay quiet until the first tap.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole game in one file |
| `sw.js` | Lets the game open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The balloons icon |

## Putting it on an iPad

The game is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/Popcorn/numbers/`.

1. Open the address in Safari.
2. Tap Share, then Add to Home Screen, then Add.
3. Open Numbers from the Home Screen; it fills the whole screen with no Safari bars.
