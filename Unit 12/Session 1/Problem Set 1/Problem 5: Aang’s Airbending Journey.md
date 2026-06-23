# Problem 5: Aang’s Airbending Journey

Aang is on a journey across a series of floating air platforms, represented by an integer array `platforms`. He starts on the first platform (index `0`), and each element in the array represents the maximum distance Aang can airbend-jump from that platform.

Write a function `aang_journey()` that returns `True` if Aang can reach the last platform, or `False` if it’s impossible.

```python
def aang_journey(platforms):
    pass
```

Example Usage:

```python
print(aang_journey([2, 3, 1, 1, 4]))
print(aang_journey([3, 2, 1, 0, 4]))
```

Example Output:

```markdown
True  
Example 1 Explanation: Aang can airbend-jump 1 step from platform 0 to platform 1, and then jump 3 steps to the last platform.

False  
Example 2 Explanation: No matter what, Aang is stuck at platform 3 because its maximum jump is 0, making it impossible to reach the last platform.
```
