# Category-Level Transition Table

| Input category | Mask update | Length |
|---|---|---|
| Uppercase A–Z | `m OR 0001` | `n + 1` |
| Lowercase a–z | `m OR 0010` | `n + 1` |
| Digit 0–9 | `m OR 0100` | `n + 1` |
| Punctuation | `m OR 1000` | `n + 1` |
| Space/control/non-ASCII | Trap/reject | No accepting transition |
| Input when length is already 16 | Trap/reject | Overflow |

End-of-input accepts iff `8 <= n <= 16` and `m = 1111`. The table groups characters by category; each state and input symbol still has exactly one next state.
