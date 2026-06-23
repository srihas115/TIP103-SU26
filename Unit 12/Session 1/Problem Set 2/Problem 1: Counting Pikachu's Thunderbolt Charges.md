# Problem 1: Counting Pikachu's Thunderbolt Charges

Pikachu is preparing for an epic battle, and Ash needs to keep track of how many Thunderbolt charges Pikachu can store in his electric pouch. Pikachu’s electric power can be represented in binary form, and the number of Thunderbolt charges corresponds to the number of `1`s in the binary representation of each number.

Given an integer `n`, return an array `ans` of length `n + 1` such that for each number `i` `(0 <= i <= n)`, `ans[i]` is the number of Thunderbolt charges (`1`’s in the binary representation) Pikachu can store.

Write a function `thunderbolt_charges()` to calculate the number of Thunderbolt charges for each number from 0 to `n`.

```python
def thunderbolt_charges(n):
    pass
```

Example Usage:

```python
print(thunderbolt_charges(2))
print(thunderbolt_charges(5))
print(thunderbolt_charges(10))
```

Example Output:

```markdown
[0, 1, 1]  
Example 1 Explanation:  
- 0 in binary is `0`, so Pikachu stores `0` Thunderbolt charges.  
- 1 in binary is `1`, so Pikachu stores `1` Thunderbolt charge.  
- 2 in binary is `10`, so Pikachu stores `1` Thunderbolt charge.

[0, 1, 1, 2, 1, 2]  
Example 2 Explanation:  
- 0 in binary is `0`, so Pikachu stores `0` Thunderbolt charges.  
- 1 in binary is `1`, so Pikachu stores `1` Thunderbolt charge.  
- 2 in binary is `10`, so Pikachu stores `1` Thunderbolt charge.  
- 3 in binary is `11`, so Pikachu stores `2` Thunderbolt charges.  
- 4 in binary is `100`, so Pikachu stores `1` Thunderbolt charge.  
- 5 in binary is `101`, so Pikachu stores `2` Thunderbolt charges.

[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]  
Example 3 Explanation:  
- 0 in binary is `0`, so Pikachu stores `0` Thunderbolt charges.  
- 1 in binary is `1`, so Pikachu stores `1` Thunderbolt charge.  
- 10 in binary is `1010`, so Pikachu stores `2` Thunderbolt charges.
```

<details>
  <summary><strong>✨ AI Hint: 1-D Dynamic Programming</strong></summary>

This problem can be solved using **dynamic programming**. (Technically, this is 1-D dynamic programming, but we often just call it dynamic programming.)

To learn more about 1-D dynamic programming, try using an AI tool like ChatGPT or GitHub Copilot to explain the topic, both conceptually and with examples in Python. You can also check out the 1-D Dynamic Programming section of the [Unit 12 Cheatsheet](#unit-12-cheatsheet).

</details>
