# Problem 1: Sorting Plants by Rarity

You are going to a plant swap where you can exchange cuttings of your plants for new plants from other plant enthusiasts. You want to bring a mix of cuttings from both common and rare plants in your collection. You track your plant collection in a binary search tree (BST) where each node has a `key` and a `val`. The `val` contains the plant name, and the `key` is an integer representing the plant's rarity. Plants are organized in the BST by their `key`.

To help choose which plants to bring, write a function `sort_plants()` which takes in the BST root `collection` and returns an array of plant nodes as tuples in the form `(key, val)` sorted from least to most rare. Sorted order can be achieved by performing an **inorder traversal** of the BST.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.  Assume the input tree is balanced when calculating time and space complexity.  

```python
class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key      # Plant rarity
        self.val = val      # Plant name
        self.left = left
        self.right = right

def sort_plants(collection):
    pass
```

Example Usage:

```python
"""
         (3, "Monstera")
        /               \
   (1, "Pothos")     (5, "Witchcraft Orchid")
        \                 /
  (2, "Spider Plant")   (4, "Hoya Motoskei")
"""

# Using build_tree() function at the top of page
values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

print(sort_plants(collection))
```

Example Output:

```markdown
[(1, 'Pothos'), (2, 'Spider Plant'), (3, 'Monstera'), (4, 'Hoya Motoskei'), (5, 'Witchcraft Orchid')]
```

<details>
  <summary><strong>✨ AI Hint: Traversing Trees</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem requires you to traverse a binary tree. For a refresher on this topic, check out the Tree Traversal section of the [Unit 8 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/8#!cheatsheet).

Still have questions? Try asking an AI tool like ChatGPT or GitHub Copilot to explain the different types of binary tree traversal. You can use the following prompt as a starting point:

*"You're an expert computer science tutor. Please explain the different types of binary tree traversal, and show me how they would each work on an example tree."*

Hint: Be sure to learn about "preorder", "postorder", and "inorder" traversals!

</details>
