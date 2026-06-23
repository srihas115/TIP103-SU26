# Problem 6: Find All Flight Routes

You are given a flight network represented as a directed acyclic graph (DAG) with `n` airports, labeled from `0` to `n - 1`. Your goal is to find all possible flight paths from airport `0` (the starting point) to airport `n - 1` (the final destination) and return them in any order.

The flight network is given as follows: `flight_routes[i]` is a list of all airports you can fly to directly from airport `i` (i.e., there is a one-way flight from airport `i` to airport `flight_routes[i][j]`).

Write a function that returns all possible flight paths from airport `0` to airport `n - 1`.

```python
def find_all_flight_routes(flight_routes):
    pass
```

Example Usage 1:

!['flight_routes_2' graph diagram](../../Unit%20Assets/find_all_flight_routes_ex1.jpg)

```python
flight_routes_1 = [[1, 2], [3], [3], []]

print(find_all_flight_routes(flight_routes_1))
```

Example Output 1:

```markdown
[[0, 1, 3], [0, 2, 3]]
Explanation: 
- There are two possible paths from airport 0 to airport 3.
- The first path is: 0 -> 1 -> 3
- The second path is: 0 -> 2 -> 3
```

Example Usage 2:

!['flight_routes_2' graph diagram](../../Unit%20Assets/find_all_flight_routes_ex2.jpg)

```python
flight_routes_2 = [[4,3,1],[3,2,4],[3],[4],[]]

print(find_all_flight_routes(flight_routes_2))
```

Example Output 2:

```markdown
[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
```
