# Problem 3: Find All Duplicate Treasure Chests in an Array

Captain Blackbeard has an integer array `chests` of length `n` where all the integers in `chests` are in the range `[1, n]` and each integer appears once or twice. Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.

```python
def find_duplicate_chests(chests):
    pass
```

Example Usage:

```python
chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
```

Example Output:

```
[2, 3]
[1]
[]
```

<details>
    <summary>AI Hint: Frequency Maps</summary>
    *Key Skill: Use AI to explain code concepts*
    
    A dictionary that maps unique values to their frequencies within a given data structure or data type is often called a**frequency map**. Frequency maps are an extremely useful problem solving tool that you will see often throughout this unit and in future units.
    
    We encourage you to learn by doing and attempt this problem before doing a deeper dive! However, if you get stuck, you can ask a generative AI tool like ChatGPT or GitHub Copilot to explain the concept.
    
    For example, you could say:
    
    *"You're an expert computer science tutor for a Python-based technical interviewing course. Please explain what a frequency map is, and provide one or more examples of simple technical interview problems in which a frequency map is useful."*
<details>