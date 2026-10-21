# Memory

The pairs game, for small kids. Turn over two cards; if the pictures match, they stay up. Find them all.

- **Small, Medium or Big:** 6, 12 or 20 cards. The app remembers the choice.
- **1 player:** the strip at the top counts pairs found and moves made.
- **2 players:** Blue and Orange take turns. The coloured frame shows whose turn it is, a match earns another go, and the one with more pairs wins.
- Every game picks fresh pictures. Matches bounce and chime; a wrong pair turns back over on its own.
- Tap Play (or anywhere on the start screen) to begin. The little house in the corner goes back to the start.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for. Nothing is stored except the size, players and sound settings.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole game in one file |
| `sw.js` | Lets the game open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The four-cards icon |

## Putting it on an iPad

The game is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/Popcorn/memory/`.

1. Open the address in Safari.
2. Tap Share, then Add to Home Screen, then Add.
3. Open Memory from the Home Screen; it fills the whole screen with no Safari bars.
