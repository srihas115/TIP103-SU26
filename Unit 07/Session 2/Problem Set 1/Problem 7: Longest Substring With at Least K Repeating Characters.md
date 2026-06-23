# Problem 7: Longest Substring With at Least K Repeating Characters

Given a string `s` and an integer `k`, use a divide and conquer approach to return the length of the longest substring of `s` such that the frequency of each character in substring is greater than or equal to `k`.

If no such substring exists, return `0`. 

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

```python
def longest_substring(s, k):
    pass
```

Example Usage:

```python
print(longest_substring("tatooine", 2))
print(longest_substring("chewbacca", 2))
```

Example Output:

```markdown
2
Example 1 Explanation: The longest substring is 'oo' as 'o' is repeated 2 times.

4
Example 2 Explanation: The longest substirng is 'acca' as both 'a' and 'c' are repeated 2 times.
```
