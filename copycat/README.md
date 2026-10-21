# Copy Cat

Four coloured pads light up one after another; copy them by tapping. Each round adds one more.

- **Watch, then tap.** While the eye is showing, the pads are playing and won't take taps. When the hand shows, it's the kid's turn. Dots under the pads fill in as they get each one right.
- **Mistakes are gentle.** A wrong pad gives a soft boop and a wobble, then the same sequence plays again for another go. After three wrong goes the sequence loses its last pad, so the game never ends — it just eases off.
- **Rounds.** The big number is the round. Every fifth round brings confetti. The best round is remembered and shown on the start screen.
- **Slow / Normal** sets the pace, and the app remembers it. Sound can be switched off on the start screen.
- On a keyboard, 1–4 tap the pads (green, red, yellow, blue), Space starts, Escape goes back to the start.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for. Nothing is stored except the pace, the sound switch and the best round.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole game: the pads, the sounds and the logic in one file |
| `sw.js` | Lets the game open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The four-pads icon |

## Putting it on an iPad

The game is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/Popcorn/copycat/`.

1. Open the address in Safari.
2. Tap Share, then Add to Home Screen, then Add.
3. Open Copy Cat from the Home Screen; it fills the whole screen with no Safari bars.
