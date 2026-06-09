# Problem 1: The Library of Alexandria

In the ancient Library of Alexandria, a temporal rift has scattered several important scrolls across different rooms. You are given a dictionary`library_catalog`that maps room names to the number of scrolls that room should have and a second dictionary`actual_distribution`that maps room names to the number of scrolls found in that room after the temporal rift.

Write a function`analyze_library()`that determines if any room has more or fewer scrolls than it should. The function should return a dictionary where the keys are the room names and the values are the differences in the number of scrolls (actual number of scrolls - expected number of scrolls). You must loop over the dictionaries to compute the differences.

```
def analyze_library(library_catalog, actual_distribution):
    pass
```

Example Usage:

```
library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}

print(analyze_library(library_catalog, actual_distribution))
```

Example Output:

```
{'Room A': 0, 'Room B': -10, 'Room C': 10, 'Room D': 0}
```

<details>
    <summary>AI Hint: Dictionaries</summary>
    *Key Skill: Use AI to explain code concepts*
    
    This question requires you to create a dictionary.
    
    If you are unfamiliar with what a dictionary is, or how to create a dictionary, you can learn about Python dictionaries using a generative AI tool, like this:
    
    *"You're an expert computer science tutor. Please explain what a dictionary is in Python, and provide a simple code example of how to create one."*
    
    After you get your answer, you can also ask follow up questions:
    
    *"How is a dictionary different from a list? Can you show me examples of both?"*
</details>

<details>
    <summary>AI Hint: Accessing Values in a Dictionary</summary>
    *Key Skill: Use AI to explain code concepts*
    
    This question will require you to use keys to access their corresponding values in a dictionary. There are two common ways to access values in a dictionary. Try asking ChatGPT or GitHub copilot:
    
    *"You're an expert computer science tutor. Please show me the two most common ways to access values in a dictionary in Python, and explain how each one works."*
    
    Then open the next hint to see the answer!
</details>

<details>
    <summary>Hint: Dictionary Access options</summary>
    The two common ways to access values in a dictionary are square bracket notation`d[key]`and the`get()`method.
    
    The Unit 2 cheatsheet includes a more thorough breakdown of these two options. If you still feel confused after reviewing the cheatsheet, try asking generative AI to help you understand!
</details>

<details>
    <summary>Hint: Accessing Keys, Values, and Key-Value Pairs</summary>
    This question will require you to loop over a dictionary. We have three options for looping over a dictionary: looping over the keys, values, or key-value pairs. To explore how to access the keys, values, and key-value pairs reference the unit cheatsheet. For specific examples of looping over a dictionary, ask a generative AI tool to provide an example or search for existing examples using a search engine.
</details>