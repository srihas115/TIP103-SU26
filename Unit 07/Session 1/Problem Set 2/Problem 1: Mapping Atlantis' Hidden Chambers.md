# Problem 1: Mapping Atlantis' Hidden Chambers

Poseidon, the ruler of Atlantis, has a map that shows various chambers hidden deep beneath the ocean. The map is currently stored as a nested list `sections`, with each section containing smaller subsections. Write a recursive function `map_chambers()` that converts the map into a nested dictionary, where each section and subsection is a key-value pair.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

```python
def map_chambers(sections):
    pass
```

Example Usage:

```python
sections = ["Atlantis", ["Coral Cave", ["Pearl Chamber"]]]
print(map_chambers(sections))
```

Example Output

```markdown
{'Atlantis': {'Coral Cave': 'Pearl Chamber'}}
```

<details>
  <summary><strong>💡 Hint: Recursion</strong></summary>

This problem requires you to understand recursion and the differences between iteration and recursion. For reference, check out the unit cheatsheet.

</details>
