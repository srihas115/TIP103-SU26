# Problem 3: Matching of Buyers with Sellers

In the mystical market, you are given a list of buyers, where each buyer has a specific amount of gold to spend. You are also given a list of sellers, where each seller has a specific price for their magical goods.

A buyer can purchase from a seller if the buyer's gold is greater than or equal to the seller's price. Additionally, each buyer can make at most one purchase, and each seller can sell their goods to at most one buyer.

Return the maximum number of transactions that can be made in the market that satisfy these conditions.

```python
def match_buyers_and_sellers(buyers, sellers):
  pass
```

Example Usage:

```python
buyers1 = [4, 7, 9]
sellers1 = [8, 2, 5, 8]
print(match_buyers_and_sellers(buyers1, sellers1))

buyers2 = [1, 1, 1]
sellers2 = [10]
print(match_buyers_and_sellers(buyers2, sellers2))
```

Example Output:

```
3
0
```