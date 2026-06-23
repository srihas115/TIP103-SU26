# Problem 3: Finding All Reachable Destinations

You are a travel coordinator for CodePath Airlines, and you're helping a customer find all possible destinations they can reach from a starting airport. The flight connections between airports are represented as an adjacency dictionary `flights`, where each key is a destination, and the corresponding value is a list of other destinations that are reachable through a direct flight.

Given a starting location `start`, return a list of all destinations reachable from the `start` location either through a direct flight or connecting flights with layovers. The list should be provided in ascending order by number of layovers required.

```python
def get_all_destinations(flights, start):
    pass
```

Example Usage:

!['flights' graph diagram](../../Unit%20Assets/finding_all_reachable_destinations.png)

```python
flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": ["Helsinki", "Reykjavik"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))
```

Example Output:

```markdown
['Beijing', 'Mexico City', 'Helsinki', 'Sydney', 'Cairo', 'New York', 'Tokyo', 
'Reykjavik']
['Helsinki', 'Cairo', 'New York', 'Reykjavik']
```

<details>
  <summary><strong>✨ AI Hint: Breadth First Search Traversal</strong></summary>

*Key Skill: Use AI to explain code concepts*

To solve this problem, it may be helpful to understand both the **queue** data structure and **breadth first search** algorithm. To learn more about these concepts, visit the Queues and Breadth First Search sections of the Cheatsheet.

If you still have questions, try explaining what you're doing, and ask an AI tool like ChatGPT or GitHub Copilot to help you understand what's confusing you. For example, you might ask:

*"I'm trying to understand how to use a queue to implement breadth first search, but I'm confused about why I wouldn't just use a list. Can you explain the difference?"*

</details>
