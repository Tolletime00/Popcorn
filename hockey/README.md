# Air Hockey

Air hockey for two small kids, or one against the iPad. The iPad lies flat on the table; Blue is at the left end, Orange at the right.

- Each player slides their own mallet with a finger, anywhere on their half of the table. Touch near the mallet and it follows your finger; touch somewhere else on your half and it comes to you.
- The puck slides, slows, bounces off the walls and flies off a mallet as hard as you hit it. It cannot leave the table except through a goal.
- A goal counts when the puck goes all the way through the bright mouth at the end of the table. The puck comes back after a second on the side that let it in.
- First to five wins, with confetti. Tap Play again for another game. The little house in the corner pauses; from there you can continue or start over.
- Holding the iPad upright turns the table on its end (Blue at the bottom, Orange at the top) so it still fits.
- **One player:** choose 1 player on the start screen and the iPad plays Orange, at Easy, Medium or Hard. Easy is slow to react, wanders off its line and lets most good shots in; Medium is a fair game; Hard reacts in about a third of a second, predicts where the puck is going, and only a quick, well-placed shot beats it. The computer reads the same physics as a finger: it slides its mallet to a chosen spot, so its hits carry its speed. The choice of players and level is remembered.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for. Nothing is stored except the sound, players and level settings.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole game: the table, the physics, the sounds and the screens in one file |
| `sw.js` | Lets the game open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The two-mallets-and-a-puck icon |

## Putting it on an iPad

The game is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/Popcorn/hockey/`.

1. Open the address in Safari.
2. Tap Share, then Add to Home Screen, then Add.
3. Open Air Hockey from the Home Screen; it fills the whole screen with no Safari bars. Lay the iPad flat, one kid at each end.
