# Problem 6: Constructing a Harmonious Sequence

You're composing a riff consisting of a sequence of musical notes. Each note is represented by an integer in the range `[1, n]`. You want to create a "harmonious" sequence that adheres to specific musical rules:
- The sequence must be a permutation of the integers from `1` to `n` (representing the notes you can use).
- For every two notes in the sequence, if you pick any three notes `note[i]`, `note[k]`, and `note[j]` such that `i < k < j`, the note at index `k` should not be exactly the midpoint between the notes at `i` and `j` (i.e., `2 * note[k]` should not equal `note[i] + note[j]`).

Given an integer `n`, return a "harmonious" sequence of notes that meets these criteria.

```python
def harmonious_sequence(n):
    pass
```

Example Usage:

```python
print(harmonious_sequence(4))
print(harmonious_sequence(5)) 
```

Example Output:

```markdown
[1, 3, 2, 4]
Example 1 Explanation: The sequence [1, 3, 2, 4] is a harmonious sequence because it is a permutation 
of [1, 2, 3, 4] and satisfies the harmonious condition.

[1, 3, 5, 2, 4]
Example 2 Explanation: The sequence [1, 3, 5, 2, 4] is a harmonious sequence because it is a permutation
 of [1, 2, 3, 4, 5] and satisfies the harmonious condition.
```

<details>
  <summary><strong>✨ AI Hint: Divide and Conquer</strong></summary>

*Key Skill: Use AI to explain code concepts*

Merge sort (and binary search!) are examples of algorithms that use the divide and conquer technique. To learn more about this topic, check out the Divide and Conquer and Merge Sort sections of the Unit Cheatsheet.

If you have more questions, try asking an AI tool like ChatGPT or GitHub Copilot to explain the divide and conquer technique.

You can ask it to provide a real-world analogy to help you understand the concept better. Once you grasp the idea, you can ask it to help you implement a divide and conquer algorithm in Python, such as merge sort or binary search.

</details>
