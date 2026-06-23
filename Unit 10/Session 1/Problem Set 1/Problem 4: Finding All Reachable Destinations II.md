# Problem 4: Finding All Reachable Destinations II

You are a travel coordinator for CodePath Airlines, and you're helping a customer find all possible destinations they can reach from a starting airport. The flight connections between airports are represented as an adjacency dictionary `flights`, where each key is a destination, and the corresponding value is a list of other destinations that are reachable through a direct flight.

Given a starting location `start`, write a function `get_all_destinations()` that uses Depth First Search (DFS) to return a list of all destinations that can be reached from `start`. The list should include both direct and connecting flights and should be ordered based on the order in which airports are visited in DFS.

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
    "Mexico City": ["Sydney"]   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))
```

Example Output:

```markdown
['Beijing', 'Mexico City', 'Sydney', 'Tokyo', 'Helsinki', 'Cairo', 'Reykjavik', 
'New York']
['Helsinki', 'Cairo', 'Reykjavik', 'New York']
```

<br>

<details>
  <summary><strong>💡 Hint: Depth First Search</strong></summary>

This problem requires you to perform a depth first search traversal of a graph. If you need a primer on how to perform DFS on a graph, check out the unit cheatsheet.

</details>
