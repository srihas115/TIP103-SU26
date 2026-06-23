# Problem 4: Maximum Value from Removing Rare Items

You are given a string `items` consisting of lowercase English letters and two integers `x` and `y`. You may repeatedly remove literal substrings from `items` to earn value:

-   Removing the substring `"ab"` earns `x` points.

-   Removing the substring `"ba"` earns `y` points.

You may perform these operations in any order and any number of times (as long as the substrings exist). Return the maximum total value you can obtain.

```python
def maximum_value(items, x, y):
  pass
```

Example Usage:

```python
s1 = "cdbcbbaaabab"
x1, y1 = 4, 5
print(maximum_value(s1, x1, y1))

s2 = "aabbaaxybbaabb"
x2, y2 = 5, 4
print(maximum_value(s2, x2, y2))
```

Example Output:

```
19
20
```