# Problem 4: 4Sum

Given an array `nums` of `n` integers and an integer `target`, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:
- `0 <= a, b, c, d < n`
- `a`, `b`, `c`, and `d` are distinct.
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in any order.

```python
def four_sum(nums, target):
    pass
```

Example Usage:

```python
nums_1 = [1,0,-1,0,-2,2]
nums_2 = [2,2,2,2,2]

print(four_sum(nums_1, 0))
print(four_sum(nums_2, 8))
```

Example Output:

```markdown
[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
[[2,2,2,2]]
```
