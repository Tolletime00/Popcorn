# Shapes

A shape sorter for small kids. Drag each shape into the hole that matches it; when they are all in, confetti.

- Each round picks four shapes (or six, from the start screen) out of a circle, square, triangle, star, heart, hexagon, diamond and oval. Every shape always has its own colour, so the star is always yellow and the heart always pink.
- The holes sit along the top in a mixed-up order; the shapes wait below. Drag a shape with a finger and let go over its hole to drop it in with a clunk and a sparkle. Let go anywhere else and it slides back; a wrong hole gives a little wobble.
- Two shapes can be dragged at once by two fingers, and a mouse works on a laptop.
- When the last shape is in: confetti, "You did it!", and a Play again pill for a fresh set. The round waits a couple of seconds before a tap starts the next one, so nobody skips the confetti. The house button in the corner goes back to the start.
- The number of shapes and the sound switch are remembered; nothing else is stored.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole game: the shapes, the holes, the sounds and the logic in one file |
| `sw.js` | Lets the game open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The four-shapes icon |

## Putting it on an iPad

The game is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/Popcorn/shapes/`.

1. Open the address in Safari.
2. Tap Share, then Add to Home Screen, then Add.
3. Open Shapes from the Home Screen; it fills the whole screen with no Safari bars.
