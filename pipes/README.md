# Pipes

A dot-connecting puzzle for an iPad, in the style of Flow Free (the classic "Numberlink" puzzle). Join each pair of coloured dots with a pipe. Pipes can't cross, and the whole board has to fill up. Fifty puzzles, from 4×4 with a handful of colours to 8×8 with long winding pipes, each with exactly one answer.

- **Levels:** the start screen is the grid of fifty. Solved ones turn green; the next one to play has a white ring; Continue jumps to it. Levels 1–8 are 4×4, 9–18 are 5×5, 19–30 are 6×6, 31–42 are 7×7, 43–50 are 8×8, and within each size they get harder.
- **Playing:** drag from a dot to draw a pipe; drag into its partner to join them. Drag back along a pipe to undo part of it, or drag another colour across it to cut it. Dots of other colours are walls. A quick swipe that jumps cells is followed as best it can be.
- **Finishing:** the level is done when every pair is joined and every square is filled, with confetti and a Next level button. The footer counts pipes joined, how much of the board is filled, and moves (a move is each time you put a finger down). Solving in as many moves as there are colours is "perfect".
- **Help:** the bulb fills in one pipe from the answer; the circling arrow clears the board.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for. Solved levels and the sound switch are remembered on the device.

## Where the puzzles come from

`gen/gen.py` carves a square grid into winding paths and puts a dot at each end of every path, so a filling solution always exists; a solver then counts solutions and keeps only puzzles with exactly one. Each puzzle is rated by how much a plain search has to work to find the answer, and the fifty were picked from the pools by size: the easiest 4×4s, a spread across 5×5 to 7×7, and the hardest 8×8s found.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole game, the fifty puzzles included, in one file |
| `sw.js` | Lets the game open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The pipes-and-dots icon |
| `gen/gen.py`, `gen/levels.json` | The puzzle maker and the fifty puzzles it picked (baked into `index.html` at build time) |

## Putting it on an iPad

The game is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/Popcorn/pipes/`.

1. Open the address in Safari.
2. Tap Share, then Add to Home Screen, then Add.
3. Open Pipes from the Home Screen.
