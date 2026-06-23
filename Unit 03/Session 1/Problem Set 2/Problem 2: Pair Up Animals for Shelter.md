# Problem 2: Pair Up Animals for Shelter

In an animal shelter, animals are paired up to share a room. Each pair has a discomfort level, which is the sum of their individual discomfort levels. The shelter's goal is to minimize the maximum discomfort level among all pairs to ensure that the rooms are as comfortable as possible.

Given a list`discomfort_levels`representing the discomfort levels of`n`animals, where`n`is even, pair up the animals into`n / 2`pairs such that:

1.  Each animal is in exactly one pair, and
2.  The maximum discomfort level among the pairs is minimized. Return the minimized maximum discomfort level after optimally pairing up the animals.

Return the minimized maximum comfort level after optimally pairing up the animals.

```python
def pair_up_animals(discomfort_levels):
  pass
```

Example Usage:

```python
print(pair_up_animals([3,5,2,3]))
print(pair_up_animals([3,5,4,2,4,6]))
```

Example Output:

```
7
8
```

### Hint: Two Pointer Technique
This problem may benefit from a algorithmic technique called the**two pointer approach**. Take a look at the unit cheatsheet for a more in-depth overview of how this technique works.