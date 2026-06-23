# Problem 5: Three Sum

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

```python
def three_sum(nums):
    pass
```

Example Usage

```python
nums = [-1, 0, 1, 2, -1, -4]
three_sum(nums)

nums = [0, 1, 1]
three_sum(nums)

nums = [0, 0, 0]
three_sum(nums)
```

Example Output:

```
[[-1, -1, 2], [-1, 0, 1]]
[]
[[0, 0, 0]]
```

<details>
    <summary>💡Hint: Sorting Lists</summary>
    This problem may benefit from knowing how to sort a list. Python provides a couple options for sorting lists and other iterables, including`sort()`and`sorted()`. Use your independent research skills or the unit cheatsheet to research how these functions work!
</details>