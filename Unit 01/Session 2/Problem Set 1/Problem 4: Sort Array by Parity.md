# Problem 4: Sort Array by Parity

Given an integer array `nums`, write a function `sort_by_parity()` that moves all the even integers to the beginning of the array, followed by all the odd integers.

Return ***any array** that satisfies this condition*.

```python
def sort_by_parity(nums):
    pass
```

Example Usage

```python
nums = [3, 1, 2, 4]
sort_by_parity(nums)

nums = [0]
sort_by_parity(nums)
```

Example Output:

```
[2, 4, 3, 1]
[0]
```

<details>
    <summary>💡 Remainders with Modulus Division</summary>
    This problem requires you to know how to find the remainder of a division operation. We can do this with something called modulus division. If you are unfamiliar with how to do this in Python, checkout the Unit 1 cheatsheet or do your own research.
</details>