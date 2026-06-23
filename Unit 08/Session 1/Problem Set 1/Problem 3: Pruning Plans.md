# Problem 3: Pruning Plans

You have a large overgrown Magnolia tree that's in desperate need of some pruning. Before you can prune the tree, you need to do a full survey of the tree to evaluate which sections need to be pruned. 

Given the `root` of a binary tree representing the magnolia, return a list of the values of each node using a postorder traversal. In a postorder traversal, you explore the left subtree first, then the right subtree, and finally the root. Postorder traversals are often used when deleting nodes from a tree. 

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    pass
```

Example Usage:

```python
"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1"))
                        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))
```

Example Output:

```markdown
['Leaf1', 'Node1', 'Leaf2', 'Leaf3', 'Node2', 'Root']
```

<details>
  <summary><strong>✨ AI Hint: Traversing Trees</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem requires you to traverse a binary tree. For a refresher on this topic, check out the Tree Traversal section of the [Unit 8 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/8#!cheatsheet).

Still have questions? Try asking an AI tool like ChatGPT or GitHub Copilot to explain the different types of binary tree traversal. You can use the following prompt as a starting point:

*"You're an expert computer science tutor. Please explain the different types of binary tree traversal, and show me how they would each work on an example tree."*

Hint: Be sure to learn about "preorder", "postorder", and "inorder" traversals!

</details>
