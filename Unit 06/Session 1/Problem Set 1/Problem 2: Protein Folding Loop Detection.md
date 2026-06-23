# Problem 2: Protein Folding Loop Detection

As a biochemist, you're studying the folding patterns of proteins, which are represented as a sequence of amino acids linked together. These proteins sometimes fold back on themselves, creating loops that can impact their function.

Given the head of a linked list `protein` where each node in the linked list represents an amino acid in the protein, return an array with the `value`s of any cycle in the list. A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

The `value`s may be returned in any order.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    pass
```

Example Usage:

![Linked list with 4 nodes and a cycle where 4th node points to 2nd node](https://courses.codepath.org/course_images/tip103/unit6_session1/protein_folding_loop_ex.png)

```python
protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next 

print(cycle_length(protein_head))
```

Example Output:

```markdown
['Gly', 'Leu', 'Val']
```

<details>
  <summary><strong>✨ AI Hint: Slow and Fast Pointers</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem requires a variation of the two-pointer technique called the slow and fast pointer technique! For reference, check out the [Unit 5 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/5#!cheatsheet).

For more help, you can use an AI tool like ChatGPT or GitHub Copilot to show you examples of the slow and fast pointer technique.

</details>

<details>
  <summary><strong>✨ AI Hint: Multiple Pass Technique</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem may require multiple traversals of the list. For reference, check out the [Unit 6 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/6#!cheatsheet).

For more help, you can use an AI tool like ChatGPT or GitHub Copilot to show you examples of the multiple pass technique.

</details>


