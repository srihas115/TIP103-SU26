# Problem 1: Counting the Layers of a Sandwich

You're working at a deli, and need to count the layers of a sandwich to make sure you made the order correctly. Each layer is represented by a nested list. Given a list of lists `sandwich` where each list `[]` represents a sandwich layer, write a recursive function `count_layers()` that returns the total number of sandwich layers. 

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

```python
def count_layers(sandwich):
    pass
```

Example Usage: 

```python
sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

print(count_layers(sandwich1))
print(count_layers(sandwich2))
```

Example Output: 

```markdown
4
5
```

<details>
  <summary><strong>💡 Hint: Recursion</strong></summary>

This problem requires you to understand recursion and the differences between iteration and recursion. For reference, check out the unit cheatsheet.

</details>
