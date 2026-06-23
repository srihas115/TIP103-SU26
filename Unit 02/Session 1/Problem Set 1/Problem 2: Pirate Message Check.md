# Problem 2: Pirate Message Check

Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message if it contains all of the letters in the alphabet. Given a string `message` containing only lowercase English letters and whitespace, write a function `can_trust_message()` that returns `True` if the message contains every letter of the English alphabet at least once, and `False` otherwise.

```python
def can_trust_message(message):
    pass
```

Example Usage:

```python
message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
```

Example Output:

```
True
False
```

<details>
    <summary>AI Hint: AI Hint: Introduction to sets</summary>
    *Key Skill: Use AI to explain code concepts*
    
    This problem may benefit from the use of a**set**. A Python set is a data type which holds an unordered, mutable collection of*unique*elements.
    
    If you are unfamiliar with what a set is, or how to create a set, you can learn about them using a generative AI tool, like this:
    
    *"You're an expert computer science tutor. Please explain what a set is in Python, and provide a simple code example of how to create one."*
    
    After you get your answer, you can also ask follow up questions:
    
    *"How is a set different from a list or dictionary? Can you show me examples of each?"*
</details>