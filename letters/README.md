# Letters

A letter hunt for small kids. A big letter and its picture sit at the top (B and a ball); six coloured tiles sit below; tap the tile with the same letter.

- The letter is said out loud ("B. B is for ball.") when it appears, and again whenever the card at the top is tapped. The letter and the picture are always on screen, so it works with the sound off too.
- A right tap bounces, cheers and fills a star; a wrong tap just wobbles and the letter is said again. Nothing is ever lost.
- Ten stars wins: confetti, a fanfare and a Play again pill.
- The start screen has ABC / abc (capitals or small letters) and A–H / A–Z (the first eight letters, or all of them), plus a sound switch. The iPad remembers the choices.
- On a keyboard, pressing the letter's key counts as a tap.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for. Nothing is stored except the settings.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole game: the letters, the pictures, the sounds and the logic in one file |
| `sw.js` | Lets the game open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The ABC tiles icon |

## Putting it on an iPad

The game is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/Popcorn/letters/`.

1. Open the address in Safari.
2. Tap Share, then Add to Home Screen, then Add.
3. Open Letters from the Home Screen; it fills the whole screen with no Safari bars.
