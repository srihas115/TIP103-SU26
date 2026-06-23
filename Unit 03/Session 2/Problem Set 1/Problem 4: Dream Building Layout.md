# Problem 4: Dream Building Layout

You are an architect tasked with designing a dream building layout. The building layout is represented by a string `s` of even length `n`. The string consists of exactly `n / 2` left walls `'['` and `n / 2` right walls `']'`.

A layout is considered balanced if and only if:

-   It is an empty space, or
-   It can be divided into two separate balanced layouts, or
-   It can be surrounded by left and right walls that balance each other out.

You may swap the positions of any two walls any number of times.

Return the minimum number of swaps needed to make the building layout balanced.

```python
def min_swaps(s):
    pass
```

Example Usage:

```python
print(min_swaps("][]["))
print(min_swaps("]]][[["))
print(min_swaps("[]"))
```

Example Output:

```
1
2
0
```