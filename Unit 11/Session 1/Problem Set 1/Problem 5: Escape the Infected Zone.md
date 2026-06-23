# Problem 5: Escape the Infected Zone

You are trapped in a rectangular zone that has been quarantined because it is infected with zombies. The infected zone borders two safe zones: the _Pacific Safety Zone_ and the _Atlantic Safety Zone_. The Pacific Safety Zone borders the left and top edges of the infected zone, while the Atlantic Safety Zone borders the right and bottom edges.

The infected zone is partitioned into a grid of square subzones, and you are given an `m x n` integer matrix `safety` where `safety[row][column]` represents the safety level of the subzone at coordinate `(row, column)`. Higher values mean the zone is safer from the zombie outbreak.

Due to constant zombie movement, survivors can only move from one zone to an adjacent zone (north, south, east, or west) if the neighboring zone's safety level is _less than or equal to_ the current zone's safety level. This means survivors can escape to a more dangerous zone but not to a safer one.

Your goal is to identify all subzones where survivors can potentially escape the island by reaching **both** the Pacific and Atlantic Safety Zones. 

Return a 2D list of grid coordinates `result` where <code>result[i] = [r<sub>i</sub>, c<sub>i</sub>]</code> denotes that survivors in zone <code>(r<sub>i</sub>, c<sub>i</sub>)</code> can escape to both the Pacific and Atlantic Safety Zones. 

```python
def escape_subzones(safety):
    pass
```

Example Usage: 

*Example 1:*
!['safety_1' matrix shown with safety zones shown and escapable subzones highlighted](../../Unit%20Assets/escape_infected_zone_ex1.png)

```python
safety_1 = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]

safety_2 = [
    [2, 1],
    [1, 2]
]

print(escape_subzones(safety_1))
print(escape_subzones(safety_2))
```

Example Output:

```markdown
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
Example 1 Explanation: Survivors can escape from several zones on the island. 
[0,4]: [0,4] -> Pacific Safety Zone 
       [0,4] -> Atlantic Safety Zone
[1,3]: [1,3] -> [0,3] -> Pacific Safety Zone 
       [1,3] -> [1,4] -> Atlantic Safety Zone
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Safety Zone 
       [1,4] -> Atlantic Safety Zone
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Safety Zone 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Safety Zone
[3,0]: [3,0] -> Pacific Safety Zone 
       [3,0] -> [4,0] -> Atlantic Safety Zone
[3,1]: [3,1] -> [3,0] -> Pacific Safety Zone 
       [3,1] -> [4,1] -> Atlantic Safety Zone
[4,0]: [4,0] -> Pacific Safety Zone 
       [4,0] -> Atlantic Safety Zone
       
[[0, 0], [0, 1], [1, 0], [1, 1]]
Example 2 Explanation: 
All four zones can reach both the Pacific and Atlantic Safety Zones:
- [0,0]: On the Pacific edge (top/left). Can move right or down to reach the Atlantic edge.
- [0,1]: On both the top (Pacific) and right (Atlantic) edges.
- [1,0]: On both the left (Pacific) and bottom (Atlantic) edges.
- [1,1]: On the Atlantic edge (bottom/right). Can move up or left to reach the Pacific edge.
```
