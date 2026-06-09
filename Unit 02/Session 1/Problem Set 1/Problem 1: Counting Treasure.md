# Problem 1: Counting Treasure

Captain Blackbeard has a treasure map with several clues that point to different locations on an island. Each clue is associated with a specific location and the number of treasures buried there. Given a dictionary`treasure_map`where keys are location names and values are integers representing the number of treasures buried at those locations, write a function`total_treasures()`that returns the total number of treasures buried on the island.

```
def total_treasures(treasure_map):
    pass
```

Example Usage:

```
treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1))
print(total_treasures(treasure_map2))
```

Example Output:

```
15
50
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
