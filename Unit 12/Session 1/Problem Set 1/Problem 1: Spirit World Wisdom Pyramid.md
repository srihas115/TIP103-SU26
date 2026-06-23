# Problem 1: Spirit World Wisdom Pyramid

In _Avatar: The Last Airbender_ the Spirit World is a parallel plane of existence where spirits live. In the Spirit World, there exists an ancient pyramid known as the Wisdom Pyramid. Each layer of the pyramid contains mystical numbers that guide the Avatar’s journey. The numbers in each layer are formed by combining the two numbers directly above them from the previous layer.

Given an integer `wisdomLevel`, return the `wisdomLevel`-th (0-indexed) row of the Wisdom Pyramid.

In the Wisdom Pyramid, each number is the sum of the two numbers directly above it from the previous row. The first row of the pyramid (layer 0) starts with the number 1.

Write a function `wisdom_pyramid()` to return the `wisdomLevel`-th row of the pyramid.

```python
def wisdom_pyramid(wisdomLevel):
    pass
```

Example Usage:

![Wisdom Pyramid](../../Unit%20Assets/pascals.gif)

```python
print(wisdom_pyramid(3))
print(wisdom_pyramid(0))
print(wisdom_pyramid(5))
```

Example Output:

```markdown
[1, 3, 3, 1]
Example 1 Explanation: The 3rd row of the Wisdom Pyramid is [1, 3, 3, 1].

[1]
Example 2 Explanation: The 0th row of the Wisdom Pyramid is [1].

[1, 5, 10, 10, 5, 1]
Example 3 Explanation: The 5th row of the Wisdom Pyramid is [1, 5, 10, 10, 5, 1].
```

<details>
  <summary><strong>✨ AI Hint: 1-D Dynamic Programming</strong></summary>

This problem can be solved using **dynamic programming**. (Technically, this is 1-D dynamic programming, but we often just call it dynamic programming.)

To learn more about 1-D dynamic programming, try using an AI tool like ChatGPT or GitHub Copilot to explain the topic, both conceptually and with examples in Python. You can also check out the 1-D Dynamic Programming section of the [Unit 12 Cheatsheet](#unit-12-cheatsheet).

</details>
