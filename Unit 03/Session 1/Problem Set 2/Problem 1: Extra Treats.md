# Problem 1: Extra Treats

At the pet adoption center, there are two groups of volunteers:

-   `'C'`— Cat Lovers
-   `'D'`— Dog Lovers

Each week, these groups vote to decide which type of pet should receive extra treats. The voting happens in rounds, following these rules:

1.  **Ban a Vote:**In each round, a volunteer can ban one volunteer from the opposite group. A banned volunteer loses all voting rights for the rest of the process.
2.  **Declare Victory:**If at any point all remaining volunteers are from the same group, that group can declare victory, and their preferred pet will receive the extra treats.

You are given a string`votes`representing the group affiliation of each volunteer. The character at index`i`is either`'C'`(Cat Lovers) or`'D'`(Dog Lovers).

Assuming each volunteer acts in order (from left to right) and the process repeats until one group wins, predict which group will eventually declare victory.

Return:

-   `"Cat Lovers"`if the Cat Lovers will win.
-   `"Dog Lovers"`if the Dog Lovers will win.

```python
def predictAdoption_victory(votes):
  pass
```

Example Usage:

```python
print(predictAdoption_victory("CD"))
print(predictAdoption_victory("CDD"))
```

Example Output:

```
Cat Lovers
Dog Lovers
```

### AI Hint: Queue

*Key Skill: Use AI to explain code concepts*

This problem may benefit from the use of a**queue**, a data structure that follows the First In, First Out (FIFO) principle.

If you are unfamiliar with queues, you can check the[Unit 3 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/3#!cheatsheet)for a refresher, or you can learn about them using a generative AI tool, like this:

*"You're an expert computer science tutor. Please explain what a queue is in Python, and provide a simple code example of how to create one."*

After you get your answer, you can also ask follow up questions:

*"How is a queue different from a list or stack? Can you show me examples of each?"*