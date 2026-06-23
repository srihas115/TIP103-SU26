# Problem 2: Charizard's Battle Power Calculation

Charizard is preparing for an important battle, and each of his moves contributes to his overall battle power. However, Charizard can either use a move to increase or decrease his power based on his strategy. Given a list of Charizard's moves, where each move has a power value, and a target battle power, your task is to determine how many different ways Charizard can combine his moves to exactly match the target battle power.

For each move in the list, you can choose to either add or subtract its power to a total sum.

For example, if `moves = [1, 2]`, one possible combination is "+1-2=-1". 

Write a function `charizard_battle_power()` to calculate the number of different ways to combine Charizard's moves to reach the target battle power.

```python
def charizard_battle_power(moves, target):
    pass
```

Example Usage:

```python
print(charizard_battle_power([2, 2, 2], 2))
print(charizard_battle_power([1, 1], 0))
```

Example Output:

```markdown
3  
Example 1 Explanation:  
There are 3 different ways for Charizard to combine his moves to achieve a total power of 2:
+2 +2 -2 = 2  
+2 -2 +2 = 2  
-2 +2 +2 = 2  

2  
Example 2 Explanation:  
There are 2 ways for Charizard to combine his moves to reach a total power of 0:
+1 -1 = 0  
-1 +1 = 0
```
