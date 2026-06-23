# Problem 5: Beautiful Collection

Your gallery has entered a competition for the most beautiful collection. Your collection is represented by a string`collection`where each artist in your gallery is represented by a character. The beauty of a collection is defined as the difference in frequencies between the most frequent and least frequent characters.

-   For example, the beauty of`"abaacc"`is`3 - 1 = 2`.

Given a string`collection`, write a function`beauty_sum()`that returns*the sum of beauty of all of its substrings (subcollections)*, not just of the collection itself.

```python
def beauty_sum(collection):
    pass
```

Example Usage:

```python
print(beauty_sum("aabcb"))
print(beauty_sum("aabcbaa"))
```

Example Output:

```
5
Example 1 Explanation: The substrings with non-zero beauty are
["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.

17
```