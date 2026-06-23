# Problem 5: Gary's Pokédollar Trading Strategy II

Gary Oak has become experienced in the Pokémon trading market, and he's ready to make as many trades as possible to maximize his Pokédollars. Each day, the prices of Pokéballs fluctuate, and Gary wants to buy and sell Pokéballs at the best times. However, after making a sale, Gary needs a day to rest before he can make another trade. This rest period is called a cooldown.

You are given a 1-indexed array `prices` where `prices[i]` represents the value of a Pokémon trade on the `ith` day. Your task is to help Gary find the maximum profit he can achieve by completing as many trades as possible, while adhering to the following rules:
- Gary can make multiple transactions (buying and selling) but cannot hold multiple trades at the same time (he must sell a Pokéball before buying again).
- After selling a Pokéball, Gary must take a cooldown and skip trading the next day.

Write a function `max_pokedollar_profit()` that returns the maximum profit Gary can make.

```python
def max_pokedollar_profit(prices):
    pass
```

Example Usage:

```python
print(max_pokedollar_profit([1, 2, 3, 0, 2]))
print(max_pokedollar_profit([1]))
```

Example Output:

```markdown
3  
Example 1 Explanation:  
Gary should buy on day 1, sell on day 2, rest on day 3, and then buy on day 4 and sell on day 5.  
The transactions are `[buy, sell, cooldown, buy, sell]`, resulting in a total profit of 3 Pokédollars.

0  
Example 2 Explanation:  
There are no profitable trades that can be made from the single-day prices.
```
