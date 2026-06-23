# Problem 7: Pruning Pothos

You have a Pothos plant represented as a binary tree, where each node in the tree represents a segment of the plant. Given the `root` of your pothos and a value `target`, you want to delete all **leaf nodes** with value `target`. 

Note that once you delete a leaf node with value `target`, if its parent node becomes a leaf node and has the value `target`, it should also be deleted. You should continue deleting nodes until you cannot.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def prune(root, target):
    pass
```

Example Usage 1:

!['pothos1' after each set of deletions](https://courses.codepath.org/course_images/tip103/unit8_session2/pruning_pothos_ex1.png)

```python
"""
         Healthy
        /       \
     Dying    Healthy
     /          /  \
   Dying     Dying  New Growth
"""

# Using build_tree() function at the top of the page
values = ["Healthy", "Dying", "Healthy", "Dying", None, "Dying", "New Growth"]
pothos1 = build_tree(values)

# Using print_tree() function at the top of the page
print_tree(prune(pothos1, "Dying"))
```

Example Output:

```plaintext
['Healthy', None, 'Healthy', None, 'New Growth']
Explanation:
Modified Tree:
Healthy
     \
     Healthy
        \
        New Growth
```

Example Usage 2:

<!-- 
This diagram is inaccurate, so the image was omitted.
-->

```python
"""
      Healthy
     /        \
   Aphids     Aphids
   /     \
 Aphids New Growth 
"""

values = ["Healthy", "Aphids", "Aphids", "Aphids", "New Growth"]
pothos2 = build_tree(values)

print_tree(prune(pothos2, "Aphids"))
```

Example Output 2:

```plaintext
['Healthy', 'Aphids', None, None, 'New Growth']

Explanation:
Modified Tree:
    Healthy
    /
Aphids
    \
    New Growth
```
