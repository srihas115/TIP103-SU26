# Problem 1: Concert Ticket Search

You are helping a friend find a concert ticket they can afford in a sorted list `ticket_prices`. Return the index of the ticket with a price closest to, but not greater than their `budget`. 

Your solution must have `O(log n)` time complexity. 

```python
def find_affordable_ticket(ticket_prices, budget):
    pass
```

Example Usage:

```python
print(find_affordable_ticket([50, 75, 100, 150], 90))
```

Example Output: 

```markdown
1
Explantion: 75 is the closest ticket price less than or equal to 90. 
It has index 1. 
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
