# Problem 5: Container with Most Honey

Christopher Robin is helping Pooh construct the biggest hunny jar possible.

Help him write a function that accepts an integer array `heights` of length `n`. The height of each element is given by `heights[i]`.

There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, heights[i])`.

Find two lines that, together with the x-axis, form the container that holds the most honey.

Return the maximum amount of honey a container can store.

**Notice** that you may not slant the container.

```python
def most_honey(heights):
    pass
```

![alt text](../../Unit%20Assets/image.png)

Example Usage

```python
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
most_honey(height)

height = [1, 1]
most_honey(height)
```

Example Output:

```
49
1
```