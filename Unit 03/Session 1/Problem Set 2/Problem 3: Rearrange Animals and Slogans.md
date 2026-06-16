# Problem 3: Rearrange Animals and Slogans

You are given a string`s`that consists of lowercase English letters representing animal names or slogans and brackets. The goal is to rearrange the animal names or slogans in each pair of matching parentheses by reversing them, starting from the innermost pair.

After processing, your result should not contain any brackets.

```
def rearrange_animal_names(s):
  pass
```

Example Usage:

```
print(rearrange_animal_names("(dribtacgod)"))
print(rearrange_animal_names("(!(love(stac))I)"))
print(rearrange_animal_names("adopt(yadot(a(tep)))!"))
```

Example Output:

```
dogcatbird
Ilovecats!
adoptapettoday!
```

### AI Hint: Stacks

*Key Skill: Use AI to explain code concepts*

This problem may benefit from the use of a **stack**, a data structure that follows the Last In, First Out (LIFO) principle.

If you are unfamiliar with stacks, you can check the [Unit 3 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/3#!cheatsheet) for a refresher, or you can learn about them using a generative AI tool, like this:

*"You're an expert computer science tutor. Please explain what a stack is in Python, and provide a simple code example of how to create one."*

After you get your answer, you can also ask follow up questions:

*"How is a stack different from a list or a queue? Can you show me examples of each?"*