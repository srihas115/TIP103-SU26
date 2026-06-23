# Problem 5: Finding the Crescendo in a Riff

You're a music producer analyzing a vocal riff in a song. The riff starts softly, builds up to a powerful high note (the crescendo), and then gradually descends. You're given an array `riff` representing the loudness of the notes in the riff. The values first increase up to the high note and then decrease.

Write a function `find_crescendo()` that returns the index of the crescendo — the highest note in the riff — using an efficient algorithm with `O(log n)`time complexity.

```python
def find_crescendo(riff):
    pass
```

Example Usage:

```python
print(find_crescendo([1, 3, 7, 12, 10, 6, 2])) 
``` 

Example Output:

```markdown
3
Explanation: The crescendo (highest note) is 12, which occurs at index 3 in the riff.
```
