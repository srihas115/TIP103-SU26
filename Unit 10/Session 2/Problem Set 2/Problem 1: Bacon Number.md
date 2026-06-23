# Problem 1: Bacon Number

[Six Degrees of Kevin Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon) is a game where you try to find a path of mutual connections between some actor or person to the actor Kevin Bacon in six steps or less. You are given an adjacency dictionary `bacon_network`, where each key represents an `actor` and the corresponding list `bacon_network[actor]` represents an actor they have worked with. Given a starting actor `celeb`, find their Bacon Number. `'Kevin Bacon'` is guaranteed to be a vertex in the graph. 

To compute an individual's Bacon Number, assume the following:
- Kevin Bacon himself has a Bacon Number of `0`.
- Actors who have worked directly with Kevin Bacon have a Bacon Number of `1`. 
- If an individual has worked with `actor_b` and `actor_b` has a Bacon Number of `n`, the individual has a Bacon Number of `n+1`. 
- If an individual cannot be connected to Kevin Bacon through a path of mutual connections, their Bacon Number is `-1`. 

```python
def bacon_number(bacon_network, celeb):
    pass
```

Example Usage:

!['bacon network' graph diagram](../../Unit%20Assets/bacon_number.png)

```python
bacon_network = {
    "Kevin Bacon": ["Kyra Sedgewick", "Forest Whitaker", "Julia Roberts", "Tom Cruise"],
    "Kyra Sedgewick": ["Kevin Bacon", "Tom Cruise"],
    "Tom Cruise": ["Kevin Bacon", "Kyra Sedgewick"],
    "Forest Whitaker": ["Kevin Bacon", "Denzel Washington"],
    "Denzel Washington": ["Forest Whitaker", "Julia Roberts"],
    "Julia Roberts": ["Denzel Washington", "Kevin Bacon", "George Clooney"],
    "George Clooney": ["Julia Roberts", "Vera Farmiga"],
    "Vera Farmiga": ["George Clooney", "Max Theriot"],
    "Max Theriot": ["Vera Farmiga", "Jennifer Lawrence"],
    "Jennifer Lawrence": ["Max Theriot"]
}

print(bacon_number(bacon_network, "Jennifer Lawrence"))
print(bacon_number(bacon_network, "Tom Cruise"))
```

Example Output:

```markdown
5
1
```

<details>
  <summary><strong>✨ AI Hint: Breadth First Search Traversal</strong></summary>

*Key Skill: Use AI to explain code concepts*

To solve this problem, it may be helpful to understand both the **queue** data structure and **breadth first search** algorithm. To learn more about these concepts, visit the Queues and Breadth First Search sections of the Cheatsheet.

If you still have questions, try explaining what you're doing, and ask an AI tool like ChatGPT or GitHub Copilot to help you understand what's confusing you. For example, you might ask:

*"I'm trying to understand how to use a queue to implement breadth first search, but I'm confused about why I wouldn't just use a list. Can you explain the difference?"*

</details>
