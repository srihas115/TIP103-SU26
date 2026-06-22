# Problem 6: Merge Intervals

You are given an array of intervals, where each interval is represented as `[start, end]`.

Write a function `merge_intervals(intervals)` that merges all overlapping intervals and returns a new array of the merged, non-overlapping intervals.

```
def merge_intervals(intervals):
    pass
```

Example Usage

```
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals)
```

Example Output:

```
[[1, 6], [8, 10], [15, 18]]
[[1, 5]]
```

<details>
    <summary>💡Hint: Sorting Lists</summary>
    This problem may benefit from knowing how to sort a list. Python provides a couple options for sorting lists and other iterables, including`sort()`and`sorted()`. Use your independent research skills or the unit cheatsheet to research how these functions work!
<details>