# Coloring

A coloring book for small kids. Tap a color, then tap a part of the picture.

- **Eight pictures:** a house, a fish, a flower, a car, a cat, a rocket, a butterfly and an ice cream. Every part is big enough for a small finger. The arrows under the picture (or ← → on a keyboard) move between them; the dots show which one you are on.
- **Twelve colors** down the side (along the bottom when the iPad is upright). White is the eraser.
- **Undo** (top right) takes back the last color. The red ✕ (bottom left) starts the picture over.
- When every part of a picture has a color, a little confetti. You can keep changing colors after that.
- Every picture's colors are kept on the device, so they are still there next time.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole app: the pictures (drawn as SVG), the palette, the sounds and the logic in one file |
| `sw.js` | Lets the app open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The crayons icon |

## Putting it on an iPad

The app is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/Popcorn/coloring/`.

1. Open the address in Safari.
2. Tap Share, then Add to Home Screen, then Add.
3. Open Coloring from the Home Screen; it fills the whole screen with no Safari bars.
