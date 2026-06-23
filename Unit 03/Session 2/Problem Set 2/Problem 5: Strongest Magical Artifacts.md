# Problem 5: Strongest Magical Artifacts

In the Mystical Market, you are given an array of magical artifacts represented by integers `artifacts`, and an integer `k`.

A magical artifact `artifacts[i]` is said to be stronger than `artifacts[j]` if `|artifacts[i] - m| > |artifacts[j] - m|` where `m` is the median strength of the artifacts. If `|artifacts[i] - m| == |artifacts[j] - m|`, then `artifacts[i]` is said to be stronger than `artifacts[j]` if `artifacts[i] > artifacts[j]`.

Return a list of the strongest `k` magical artifacts in the Mystical Market. Return the answer in any arbitrary order.

```python
def get_strongest_artifacts(artifacts, k):
  pass
```

Example Usage:

```python
print(get_strongest_artifacts([1, 2, 3, 4, 5], 2))
print(get_strongest_artifacts([1, 1, 3, 5, 5], 2))
print(get_strongest_artifacts([6, 7, 11, 7, 6, 8], 5))
```

Example Output:

```
[5, 1]
[5, 5]
[11, 8, 6, 6, 7]
```