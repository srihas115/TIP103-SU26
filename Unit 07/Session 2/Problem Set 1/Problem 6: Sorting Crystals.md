# Problem 6: Sorting Crystals

The Jedi Council has tasked you with organizing a collection of ancient kyber crystals. Each crystal has a unique power level represented by an integer. The kyber crystals are stored in a holocron in a completely random order, but to harness their true power, they must be arranged in ascending order based on their power levels.

Given an unsorted list of crystal power levels `crystals`, write a function that returns `crystals` as a sorted list. Your function must have `O(nlog(n))` time complexity.

```python
def sort_crystals(crystals):
    pass
```

Example Usage:

```python
print(sort_crystals([5, 2, 3, 1]))
print(sort_crystals([5, 1, 1, 2, 0, 0]))
```

Example Output:

```markdown
[1, 2, 3, 5]
[0, 0, 1, 1, 2, 5]
```

<details>
  <summary><strong>✨ AI Hint: Divide and Conquer</strong></summary>

*Key Skill: Use AI to explain code concepts*

Merge sort (and binary search!) are examples of algorithms that use the divide and conquer technique. To learn more about this topic, check out the Divide and Conquer and Merge Sort sections of the Unit Cheatsheet.

If you have more questions, try asking an AI tool like ChatGPT or GitHub Copilot to explain the divide and conquer technique.

You can ask it to provide a real-world analogy to help you understand the concept better. Once you grasp the idea, you can ask it to help you implement a divide and conquer algorithm in Python, such as merge sort or binary search.

</details>

<details>
  <summary><strong>✨ AI Hint: Merge Sort</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem requires you to understand the merge sort algorithm. To learn more about this topic, check out the Merge Sort section of the Unit Cheatsheet.

For more help, you can use an AI tool like ChatGPT or GitHub Copilot to show you examples of the merge sort algorithm, and break down each step of the process.

</details>
