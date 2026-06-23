# Problem 1: Escaping the Sea Caves

You are given the `root` of a binary tree representing possible route through a system of sea caves. You recall that so long as you take the leftmost branch at every fork in the route, you'll find your way back home. Write a function `leftmost_path()` that returns an array with the value of each node in the leftmost path. ***If there is no left child, return only the root node value (the leftmost path in this case is just the root node).***

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def leftmost_path(root):
    pass
```

Example Usage:

```python
"""
        CaveA
       /      \
    CaveB    CaveC
    /   \        \
CaveD CaveE     CaveF  
"""
system_a = TreeNode("CaveA", 
                  TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")), 
                          TreeNode("CaveC", None, TreeNode("CaveF")))

"""
  CaveA
      \
      CaveB
        \
        CaveC  
"""
system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))

print(leftmost_path(system_a))
print(leftmost_path(system_b))
```

Example Output:

```markdown
['CaveA', 'CaveB', 'CaveD']
['CaveA']
```

<details>
  <summary><strong>✨ AI Hint: Binary Trees</strong></summary>

*Key Skill: Use AI to explain code concepts*

This problem requires you to understand binary trees. For a refresher on this topic, check out the Binary Trees section of the [Unit 8 Cheatsheet](https://courses.codepath.org/courses/tip103/unit/8#!cheatsheet).

If you need more help, try asking an AI tool like ChatGPT or GitHub Copilot to explain the concept of binary trees using a real-world analogy, and any following questions you have.

Once you grasp the idea, you can ask it to show you examples of binary trees in Python.

</details>
