# Budget

A monthly budget on an iPad or an iPhone: recurring bills and income, card spending by account, and what each month left over. On an iPad the four sections sit in a sidebar and the forms open as dialogs; on an iPhone they are the tabs along the bottom and sheets that slide up. Same app, same address, same backup file.

- **Month:** one month at a time (arrows to move between months). The monthly limit, how far the recurring items ran over or under their estimates, what went on each account, a Savings row for whatever you put away that month (tap it to enter the amount), and the balance. The column reads like a sum: money in is plain, money out has a minus.
- **Recurring:** paychecks and bills with what you expect each to be, in sections you name. As the month goes on, tap an item and enter what it actually was.
- **Accounts:** BofA, Amex, Marriott, Capital One, Chase and Amazon, each the same screen. A Pending section comes first, for charges the card still shows as pending; then each month, and under it a grey line for every day (this month shows every day so far, with something on it or not; older months only the days that had something). The + on a day adds an expense to that day, the + on Pending adds a pending one, and the Add expense button at the top asks for the date. Drag an expense by the lines at its end, or hold it, to move it to another day, into or out of Pending, or to another spot in its day. Tap one to change it, switch it between Pending and Posted, or delete it. A pending charge counts into its month like any other.

Amounts are typed with the decimal already in place: 4230 is $42.30. The screens show whole dollars (42.30 shows as $42), but the cents are kept and go into every total.
- **Savings:** what each month left over, as a list with its total at the top. Add a month by hand, or tap the current month's line to save the balance the app worked out.

It is a web app that lives on the Home Screen: no App Store, no Mac, nothing to pay for.

## The arithmetic

- **Monthly limit** = expected income − expected recurring expenses, from the Recurring tab.
- **Actual recurring vs estimate** = how much the month came in under the plan, over every item with an actual entered: for an expense, estimate − actual; for income, actual − estimate. Positive (green) means under the plan, negative (red) means over.
- **Each account** = the expenses on that account dated in the month, pending ones included, less any refunds.
- **Savings** (the Month tab row) = what you put away that month, entered by hand. It counts like an expense.
- **Balance** = monthly limit + actual recurring vs estimate − the accounts − savings.
- **Spending limit per day** = (monthly limit − savings) ÷ the days in the month, in grey under the balance.
- **Expected balance** = (monthly limit − savings) − spending limit per day × the days gone so far (today included): what would be left if the limit were spent evenly so the month ended on exactly zero. A finished month shows $0; one not started yet shows the whole limit.

Everything stays on the device it was typed into. The three dots back it all up to one file for OneDrive and restore from it; that file is also how the numbers move from an iPhone to an iPad.

## How it is put together

| File | What it is |
| --- | --- |
| `index.html` | The whole app: screens, styles and logic in one file |
| `sw.js` | Lets the app open with no signal |
| `manifest.webmanifest` | The app's name and icon for the Home Screen |
| `apple-touch-icon.png`, `icon-512.png` | The piggy bank icon |

## Moving it to an iPad (or a new iPhone)

Nothing has to be rebuilt. The app is this folder's GitHub Pages address: `https://YOUR-USERNAME.github.io/Popcorn/budget/`.

1. On the iPhone: the three dots, Back up, and save `Budget backup.json` to OneDrive.
2. On the iPad: open the address in Safari, tap Share, then Add to Home Screen. Keep "Open as Web App" on and tap Add.
3. Open Budget from the Home Screen. It asks whether you already use Budget on an iPhone: tap Restore from a backup and pick `Budget backup.json` from OneDrive. (Later on, the same thing is under the three dots.)

Each device keeps its own copy, so after the move keep entering on the one you restored to, or back up from one and restore on the other whenever you switch.
