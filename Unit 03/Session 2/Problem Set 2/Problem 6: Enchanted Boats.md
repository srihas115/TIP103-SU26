# Problem 6: Enchanted Boats

You are given an array creatures where `creatures[i]` is the magical power of the `i`-th creature, and an infinite number of enchanted boats where each boat can carry a maximum magical load of `limit`. Each boat carries at most two creatures at the same time, provided the sum of the magical power of those creatures is at most `limit`.

Return the minimum number of enchanted boats required to carry every magical creature.

```python
def num_enchanted_boats(creatures, limit):
  pass
```

Example Usage:

```python
print(num_enchanted_boats([1, 2], 3))
print(num_enchanted_boats([3, 2, 2, 1], 3))
print(num_enchanted_boats([3, 5, 3, 4], 5))
```

Example Output:

```
1
3
4
```