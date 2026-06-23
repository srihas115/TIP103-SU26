# Problem 2: Finding the Longest Sequence of Trident Gems

The people of Atlantis are collecting rare Trident Gems as they explore the ocean. The gems are arranged in a sequence of integers representing their value. Write a recursive function that returns the length of the consecutive sequence of gems where each subsequent value increases by exactly 1. 

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

```python
def longest_trident_sequence(gems):
    pass
```

Example Usage:

```python
print(longest_trident_sequence([1, 2, 3, 2, 3, 4, 5, 6]))
print(longest_trident_sequence([5, 10, 7, 8, 1, 2]))
```

Example Output:

```markdown
5
Example 1 Explanation: longest sequence is 2, 3, 4, 5, 6

2
Example 2 Explanation: longest sequence is 7, 8 or 1, 2
```

<details>
  <summary><strong>💡 Hint: Recursive Helpers</strong></summary>

Many recursive solutions can benefit from or even require the use of helper functions. To learn more about recursive helper functions, check out the Recursive Driver and Helper Functions sections of the unit cheatsheet.

</details>
