# Problem 6: Word Ladder

A transformation sequence from word `begin_word` to word `end_word` using an array `word_list` is a sequence of words <code>begin_word -> s<sub>1</sub> -> s<sub>2</sub> -> ... -> s<sub>k</sub></code> such that:

- Every adjacent pair of words differs by a single letter.
- Every <code>s<sub>i</sub></code> for `1 <= i <= k` is in `word_list`. Note that `begin_word` does not need to be in `word_list`.
- <code>s<sub>k</sub> == end_word</code>

Given two words, `begin_word` and `end_word`, and an array `word_list`, return the number of words in the shortest transformation sequence from `begin_word` to `end_word`, or `0` if no such sequence exists.

```python
def ladder_length(begin_word, end_word, word_list):
    pass
```

Example Usage:

```python
word_list_1 = ["hot","dot","dog","lot","log","cog"]
word_list_2 = ["hot","dot","dog","lot","log"]

print(ladder_length("hit", "cog", word_list_1))
print(ladder_length("hit", "cog", word_list_2))
```

```markdown
5
Example 1 Explanation: One shortest transformation sequence is 
"hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

0
Example 2 Explanation: The end_word "cog" is not in word_list, therefore there is no valid 
transformation sequence.
```

<details>
  <summary><strong>💡 Hint: Leetcode Hard</strong></summary>

For an extra challenge on the last problem of the course, this is a Leetcode Hard problem! This is not in scope for the assessments, but meant as an extra fun challenge to continue to push your problem solving skills!

</details>
