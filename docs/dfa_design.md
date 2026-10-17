# DFA Design

A DFA is `M = (Q, Σ, δ, q0, F)`.

- `Q`: states `(n,m)` plus a rejecting trap state.
- `Σ`: printable ASCII characters from `!` through `~`.
- `δ`: deterministic transition function.
- `q0`: `(0,0000)`.
- `F`: states `(n,1111)` where `8 <= n <= 16`.

`n` counts characters consumed. `m` is a four-bit mask: uppercase `0001`, lowercase `0010`, digit `0100`, punctuation `1000`. Reading a character increments `n` and sets the corresponding bit. If a character is outside the alphabet or the next character would exceed length 16, transition to the trap state. The trap state loops to itself. Accept at end only if length is 8–16 and all four bits are set.

Example `Admin@123`: uppercase appears at `A`, lowercase appears at `d`, punctuation appears at `@`, digits appear at `1`, `2`, `3`. Final length is 9 and mask is `1111`, so accept.

This tuple representation is a compact way to describe a finite automaton without drawing hundreds of individual states.
