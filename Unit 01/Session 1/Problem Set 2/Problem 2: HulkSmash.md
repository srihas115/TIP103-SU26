# Problem 2: HulkSmash
Write a function `hulk_smash()` that accepts an integer `n` and returns a 1-indexed string array `answer` where:

-   `answer[i] == "HulkSmash"` if `i` is divisible by `3` and `5`.
-   `answer[i] == "Hulk"` if `i` is divisible by `3`.
-   `answer[i] == "Smash"` if `i` is divisible by `5`.
-   `answer[i] == i` (as a string) if none of the above conditions are true.

```python
def hulk_smash(n):
    pass
```

Example Usage:

```python
n = 3
hulk_smash(n)

n = 5
hulk_smash(n)

n = 15
hulk_smash(n)
```

Example Output:

```
["1", "2", "Hulk"]
["1", "2", "Hulk", "4", "Smash"]
["1", "2", "Hulk", "4", "Smash", "Hulk", "7", "8", "Hulk", "Smash", "11", "Hulk", "13", "14", "HulkSmash"]
```