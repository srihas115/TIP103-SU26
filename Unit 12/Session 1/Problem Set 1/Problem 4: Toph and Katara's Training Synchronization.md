# Problem 4: Toph and Katara's Training Synchronization

Toph and Katara are practicing their bending skills together. Both have different training sequences, but they want to synchronize their moves as much as possible. A synchronized sequence is a common subsequence that appears in both Toph’s and Katara’s training routines while preserving the order of the moves.

Given two strings `katara_moves` and `toph_moves`, return the length of their longest common subsequence. If there is no common subsequence, return `0`.

A subsequence of a string is a new string generated from the original string by deleting some characters (without changing the relative order of the remaining characters).

Using dynamic programming, write a function `training_synchronization()` to calculate the longest common subsequence.

```python
def training_synchronization(katara_moves, toph_moves):
    pass
```

Example Usage:

```python
print(training_synchronization("waterbend", "earthbend"))
print(training_synchronization("bend", "bend"))
print(training_synchronization("fire", "air"))
```

Example Output:

```markdown
6  
Example 1 Explanation: The longest common subsequence is "erbend" and its length is 6.

4  
Example 2 Explanation: The longest common subsequence is "bend" and its length is 4.

2  
Example 3 Explanation: The longest common subsequence is "ir" and its length is 2.
```

<details>
  <summary><strong>✨ AI Hint: 2-D Dynamic Programming</strong></summary>

Because the solution to this problem depends on two different variables, we'll need **2-D dynamic programming** to solve this problem.

To learn more about 2-D dynamic programming, try using an AI tool like ChatGPT or GitHub Copilot to explain the topic, both conceptually and with examples in Python. You can also check out the 2-D Dynamic Programming section of the [Unit 12 Cheatsheet](#unit-12-cheatsheet).

Note that 2-D dynamic programming is **only in scope for TIP103 Assessments**. It is just an extra challenge for TIP102 students 😊.

</details>
