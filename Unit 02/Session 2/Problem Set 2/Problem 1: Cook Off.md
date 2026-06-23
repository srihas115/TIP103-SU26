# Problem 1: Cook Off

In a reality TV show, contestants are challenged to do the best recreation of a meal cooked by an all-star judge using limited resources. The meal they must recreate is represented by the string`target_meal`. The contestants are given a collection of ingredients represented by the string`ingredients`.

Help the contestants by writing a function`max_attempts()`that returns the maximum number of copies of`target_meal`they can create using the given`ingredients`. You can take some letters from`ingredients`and rearrange them to form new strings.

```python
def max_attempts(ingredients, target_meal):
    pass
```

Example Input:

```python
ingredients1 = "aabbbcccc"
target_meal1 = "abc"

ingredients2 = "ppppqqqrrr"
target_meal2 = "pqr"

ingredients3 = "ingredientsforcooking"
target_meal3 = "cooking"
```

Example Output:

```
2
3
1
```

<details>
    <summary>AI Hint: Representing Infinite Values</summary>

    *Key Skill: Use AI to explain code concepts*
    
    To solve this problem, it may be helpful to know how to represent**positive or negative infinity**in Python. TO learn more, take a look at the Infinity section of the[Unit 9 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/9#!cheatsheet).
    
    If you still have questions, try asking an AI tool like ChatGPT or GitHub Copilot to explain more about positive and negative infinity. For example, you might ask:
    
    *"What is a common use case for positive or negative infinity in a program?"*
</details>