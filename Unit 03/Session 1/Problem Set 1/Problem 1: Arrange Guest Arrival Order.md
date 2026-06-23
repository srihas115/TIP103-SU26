# Problem 1: Arrange Guest Arrival Order

You are organizing a prestigious event, and you must arrange the order in which guests arrive based on a set of instructions.

The instructions are provided as a 0-indexed string `arrival_pattern` of length `n`, consisting of the characters:

-   `'I'` - The next guest should have a **higher** number than the previous guest.
-   `'D'` - The next guest should have a **lower** number than the previous guest.

You need to create a string `guest_order` of length `n + 1` that satisfies the following conditions:

1.  `guest_order` contains each number from `1` to `str(n + 1)` exactly once. These numbers represent the guests' assigned numbers.
2.  For every index `i` from `0` to `n - 1`:
    -   If `arrival_pattern[i] == 'I'`, then `guest_order[i] < guest_order[i + 1]`.
    -   If `arrival_pattern[i] == 'D'`, then `guest_order[i] > guest_order[i + 1]`.
3.  Among all valid orders, return the [lexicographically](https://en.wikipedia.org/wiki/Lexicographic_order) smallest one.

```python
def arrange_guest_arrival_order(arrival_pattern):
  pass
```

Example Usage:

```python
print(arrange_guest_arrival_order("IIIDIDDD"))
print(arrange_guest_arrival_order("DDD"))
```

Example Output:

```
123549876
4321
```

### AI Hint: Stacks
*Key Skill: Use AI to explain code concepts*

This problem may benefit from the use of a **stack**, a data structure that follows the Last In, First Out (LIFO) principle.

If you are unfamiliar with stacks, you can check the [Unit 3 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/3#!cheatsheet) for a refresher, or you can learn about them using a generative AI tool, like this:

*"You're an expert computer science tutor. Please explain what a stack is in Python, and provide a simple code example of how to create one."*

After you get your answer, you can also ask follow up questions:

*"How is a stack different from a list or a queue? Can you show me examples of each?"*

