# Budget

A monthly budget on an iPhone: recurring bills and income, card spending by account, and what each month left over.

- **Month:** one month at a time (arrows to move between months). The monthly limit, how far the recurring items ran over or under their estimates, what went on each account, and the balance.
- **Recurring:** paychecks and bills with what you expect each to be, in sections you name. As the month goes on, tap an item and enter what it actually was.
- **Accounts:** BofA, Amex, Marriott, Capital One, Chase and Amazon, each the same screen. Expenses sit under their month and, within it, under a grey line for each day; the + on a day adds an expense to that day (the Add expense button at the top still asks for the date). Drag an expense by the lines at its end, or hold it, to move it to another day or another spot in its day. Tap one to change or delete it.
- **Savings:** what each month left over, as a list with its total at the top. Add a month by hand, or tap the current month's line to save the balance the app worked out.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for.

## The arithmetic

- **Monthly limit** = expected income − expected recurring expenses, from the Recurring tab.
- **Actual recurring vs estimate** = how much the month came in under the plan, over every item with an actual entered: for an expense, estimate − actual; for income, actual − estimate. Positive (green) means under the plan, negative (red) means over.
- **Each account** = the expenses on that account dated in the month, less any refunds.
- **Balance** = monthly limit + actual recurring vs estimate − the accounts.

Everything stays on the phone. The three dots back it all up to one file for OneDrive and restore from it.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole app: screens, styles and logic in one file |
| `sw.js` | Lets the app open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The piggy bank icon |

## Getting it back on a new phone

Nothing has to be rebuilt. The app is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/Popcorn/budget/`.

1. Open the address in Safari on the new iPhone.
2. Tap Share, then Add to Home Screen. Keep "Open as Web App" on and tap Add.
3. Open Budget from the Home Screen.
4. Tap the three dots, choose "Restore from a backup" and pick `Budget backup.json` from OneDrive.
