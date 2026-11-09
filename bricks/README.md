# Bricks

A brick breaker for an iPad. Slide a finger anywhere on the board and the paddle follows it; bounce the ball and break every brick to clear the level. Forty levels, laid out the same way every time, easy to begin with and hard by the end.

- **Levels:** the start screen is the grid of forty. Cleared ones turn green, the next one has a white ring, and the ones beyond it are locked until you get there; Continue jumps to the next. Early levels have three rows of bricks, a slow ball and a wide paddle. As you go: more rows and columns, a faster ball, a narrower paddle, bricks that take two or three hits (a white band for each hit still to go), and steel bricks that never break and just get in the way. Each level is one of twelve shapes — a wall, stripes, a checkerboard, a pyramid, a diamond, an arch, a creature.
- **Playing:** tap to launch. Where the ball lands on the paddle sets its angle: the middle sends it straight up, the ends send it out wide. The ball gets a little quicker with every hit of the paddle, up to a point. Three balls a level; lose them all and it's "Try again" on the same level, nothing lost.
- **Good things fall** from some bricks from level 4 on; catch them with the paddle: WIDE (a wider paddle for a while), SLOW (a slower ball for a while), x3 (every ball splits in three), +1 (another ball).
- **Finishing:** every breakable brick gone, confetti, Next level. Points for bricks and a bonus for the level, shown as you go.
- Arrow keys, Space and Esc work too, for a laptop. A tall screen stands the board upright.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for. Cleared levels and the sound switch are remembered on the device; "Start over" on the levels screen forgets them.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole game in one file: the forty levels are made from a recipe (level number → rows, speed, paddle, shape) |
| `sw.js` | Lets the game open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The bricks-ball-and-paddle icon |

## Putting it on an iPad

The game is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/Popcorn/bricks/`.

1. Open the address in Safari.
2. Tap Share, then Add to Home Screen, then Add.
3. Open Bricks from the Home Screen.
