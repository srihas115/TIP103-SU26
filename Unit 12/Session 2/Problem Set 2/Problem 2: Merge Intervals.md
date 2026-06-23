# Problem 2: Merge Intervals

Given an array of intervals where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

```python
def merge(intervals):
    pass
```

Example Usage:

```python
intervals_1 = [[1,3],[2,6],[8,10],[15,18]]
intervals_2 = [[1,4],[4,5]]

print(merge(intervals_1))
print(merge(intervals_2))
```

Example Output: 

```markdown
[[1,6],[8,10],[15,18]]
Example 1 Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

[[1,5]]
Example 2 Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```
