# Problem 2: Grecian Artifacts

You've spent your last few trips exploring different periods of Ancient Greece. During your travels, you discover several interesting artifacts. Some artifacts appear in multiple time periods, while others in just one.

You are given two lists of strings`artifacts1`and`artifacts2`representing the artifacts found in two different time periods. Write a function`find_common_artifacts()`that returns a list of artifacts common to both time periods.

```
def find_common_artifacts(artifacts1, artifacts2):
    pass
```

Example Usage:

```
artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

print(find_common_artifacts(artifacts1, artifacts2))
```

Example Output:

```
 ["Golden Vase", "Bronze Shield"]
```

<details>
    <summary>AI Hint: Introduction to sets</summary>
    *Key Skill: Use AI to explain code concepts*
    
    This problem may benefit from the use of a**set**. A Python set is a data type which holds an unordered, mutable collection of*unique*elements.
    
    If you are unfamiliar with what a set is, or how to create a set, you can learn about them using a generative AI tool, like this:
    
    *"You're an expert computer science tutor. Please explain what a set is in Python, and provide a simple code example of how to create one."*
    
    After you get your answer, you can also ask follow up questions:
    
    *"How is a set different from a list or dictionary? Can you show me examples of each?"*
</details>