# Problem 2: Aang and Zuko’s Elemental Duel

Aang and Zuko take turns in a strategic duel to control the elements, with Aang going first. The duel begins with a number `n` representing the strength of the elements on the battlefield.

On each turn, a player must:
1. Choose any `x` such that `0 < x < n` and `n % x == 0`.
2. Reduce the battlefield’s strength by `x`, replacing `n` with `n - x`.

If a player cannot make a move, they lose the duel.

Write a function `aang_wins()` that accepts an integer `n` and returns `True` if Aang wins the duel (assuming both Aang and Zuko play optimally), and `False` otherwise.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

```python
def aang_wins(n):
    pass
```

Example Usage:

```python
print(aang_wins(2))
print(aang_wins(3))
```

Example Output: 

```markdown
True
Example 1 Explanation: Aang reduces the strength by 1, and Zuko has no more moves.

False
Example 2 Explanation: Aang reduces the strength by 1, then Zuko does the same, leaving 
Aang with no moves.
```
