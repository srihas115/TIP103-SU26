# Problem 1: Find Millenium Falcon Part I

Han Solo's ship, the Millenium Falcon, has broken down and he's searching for a specific replacement part. As a repair shop owner helping him out, write a function `check_stock()` that takes in a sorted list `inventory` where each element is an integer ID of a part you stock in your shop, and an integer `part_id` representing the integer ID of the part Han Solo is looking for. Return `True` if the `part_id` is in `inventory` and `False` otherwise.

Your solution must have `O(log n)` time complexity.

```python
def check_stock(inventory, part_id):
    pass
```

Example Usage:

```python
print(check_stock([1, 2, 5, 12, 20], 20))
print(check_stock([1, 2, 5, 12, 20], 100))
```

Example Ouput:

```markdown
True
False
```

<details>
  <summary><strong>✨ AI Hint: Binary Search</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem requires you to understand the binary search algorithm. To learn more about this topic, check out the Binary Search section of the Unit Cheatsheet.

For more help, you can use an AI tool like ChatGPT or GitHub Copilot to show you examples of the binary search algorithm. Try asking it to explain the concept first, using a real-world analogy. Once you understand the concepts, you can ask it to help you understand how to implement it in Python.

</details>

<details>
  <summary><strong>💡 Hint: `O(log n)` Time Complexity</strong></summary>

This problem lists the constraint that the solution has `O(log n)` or logarithmic time complexity. To learn more about what that means, take a look at the Logarithmic Time Complexity section of the unit cheatsheet. We recommend implementing your solution using binary search, then reading more about this time complexity **after** attempting this problem.

</details>
