# Problem 3: Race Results

Given a list `race_results` of `Player` objects where the first player in the list came first in the race, the second player in the list came second, etc., write a function `print_results()` that prints the players in place.

```python
class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
    # ... methods from previous problems

def print_results(race_results):
    pass
```

Example Usage:

```python
peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

print_results(race_one)
```

Example Output:

```markdown
1. Peach
2. Mario
3. Luigi
```
