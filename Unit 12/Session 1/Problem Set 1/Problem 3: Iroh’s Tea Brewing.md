# Problem 3: Iroh’s Tea Brewing

Uncle Iroh is experimenting with various ingredients to brew the strongest tea. He has a list of ingredients, each with a specific strength value, represented by an integer array `ingredients`. Some ingredients increase the tea's strength (positive values), while others weaken it (negative values). Iroh needs to find the combination of consecutive ingredients that results in the tea with the highest strength value.

Write a function `strongest_tea()` to help Uncle Iroh find the subarray of consecutive ingredients that results in the largest product of strengths, and return that product.

```python
def strongest_tea(ingredients):
    pass
```

Example Usage:

```python
print(strongest_tea([1, 2, -3, 4]))
print(strongest_tea([-2, -1]))
```

Example Output:

```markdown
4  
Example 1 Explanation: The strongest tea Iroh can brew uses only the last ingredient with strength 4.

2  
Example 2 Explanation: The strongest tea Iroh can brew uses both ingredients: -2 and -1 (-2 * -1 is 2).
```
