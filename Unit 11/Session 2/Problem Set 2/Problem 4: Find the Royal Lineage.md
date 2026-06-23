# Problem 4: Find the Royal Lineage

In the kingdom, the royal family is structured in a lineage represented by a Directed Acyclic Graph (DAG) with `n` members, where each member is identified by a string representing their name. 

You are given a list of relationships in the form of a 2D array `relationships`, where `relationships[i] = [elder_name, descendant_name]` indicates that there is a unidirectional bond between `elder_name` and `descendant_name`. This means that `elder_name` is an ancestor of `descendant_name`.

Your task is to  return a dictionary with the complete royal lineage of each member. For each member, return a list of all their ancestors sorted alphabetically. A member `u` is an ancestor of another member `v` if `u` can reach `v` through the set of family ties.

```python
def find_kingdom_lineage(names, relationships):
    pass
```

Example Usage:

*Example 1:*
![Example 1 graph diagram](../../Unit%20Assets/royal_lineage_ex1.png)

```python
names_1 = ["Henry", "Elizabeth", "George", "Mary", "Charles", "William"]
relationships_1 = [["Henry", "Mary"], ["Elizabeth", "Mary"], ["George", "Mary"], ["Charles", "William"], ["William", "Mary"]]

names_2 = ["Alice", "Bob", "Catherine", "Diana", "Edward"]
relationships_2 = [["Alice", "Bob"], ["Alice", "Catherine"], ["Bob", "Diana"], ["Catherine", "Diana"], ["Diana", "Edward"]]

print(find_kingdom_lineage(names_1, relationships_1))
print(find_kingdom_lineage(names_2, relationships_2))
```

Example Output:

```markdown
{
    "Henry": [],
    "Elizabeth": [],
    "George": [],
    "Mary": ["Elizabeth", "George", "Henry", "William"],
    "Charles": [],
    "William": ["Charles"]
}
Example 1 Explanation:
- Henry, Elizabeth, George, and Charles have no ancestors.
- Mary has ancestors Elizabeth, George, Henry, and William, sorted alphabetically.
- William has ancestor Charles.

{
    "Alice": [],
    "Bob": ["Alice"],
    "Catherine": ["Alice"],
    "Diana": ["Alice", "Bob", "Catherine"],
    "Edward": ["Alice", "Bob", "Catherine", "Diana"]
}
Example 2 Explanation:
- Alice has no ancestors.
- Bob has ancestor Alice.
- Catherine has ancestor Alice.
- Diana has ancestors Alice, Bob, and Catherine.
- Edward has ancestors Alice, Bob, Catherine, and Diana.
```

<details>
  <summary><strong>✨ AI Hint: Topological Sort</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem may be solved with topological sort. Check out the Advanced section of the [Unit 11 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/11#!cheatsheet) for more information.

If you need more info, you can ask an AI tool like ChatGPT or GitHub Copilot to help you understand topological sort. For example, you can ask:

*"What is topological sort, and when is it useful for solving coding problems?"*

*"Can you walk me through an example of topological sort in action?"*

</details>
