# Problem 5: Heist
The legendary outlaw Robin Hood is looking for the target of his next heist. Write a function `wealthiest_customer()` that accepts an `m x n` 2D integer matrix `accounts` where `accounts[i][j]` is the amount of money the `ith` customer has in the `jth` bank. Return a list `[i, w]` where `i` is the 0-based index of the wealthiest customer and `w` is the total wealth of the wealthiest customer.

If multiple customers have the highest wealth, return the index of any customer.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

```python
def wealthiest_customer(accounts):
    pass
```

Example Usage:

```python
accounts = [
    [1, 2, 3],
    [3, 2, 1]
]
wealthiest_customer(accounts)

accounts = [
    [1, 5],
    [7, 3],
    [3, 5]
]
wealthiest_customer(accounts)

accounts = [
    [2, 8, 7],
    [7, 1, 3],
    [1, 9, 5]
]
wealthiest_customer(accounts)
```

Example Output:

```
[0, 6]
[1, 10]
[0, 17]
```