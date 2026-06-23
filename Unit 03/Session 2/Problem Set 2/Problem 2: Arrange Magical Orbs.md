# Problem 2: Arrange Magical Orbs

In the mystical market, you have a collection of magical orbs, each of which is colored red, white, or blue. Your task is to arrange these orbs in a specific order so that all orbs of the same color are adjacent to each other. The colors should be ordered as red, white, and blue.

We will use the integers 0, 1, and 2 to represent the colors red, white, and blue, respectively.

You must arrange the orbs in-place without using any library's sorting function.

```python
def arrange_magical_orbs(orbs):
  pass
```

Example Usage:

```python
orbs1 = [2, 0, 2, 1, 1, 0]
arrange_magical_orbs(orbs1)
print(orbs1)

orbs2 = [2, 0, 1]
arrange_magical_orbs(orbs2)
print(orbs2)
```

Example Output:

```
[0, 0, 1, 1, 2, 2]
[0, 1, 2]
```