# Problem 1: Populating Next Right Pointers in Each Node

You are given the `root` of a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

```python
class TreeNode():
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
```

Populate each `next` pointer to point to its next right node. If there is no next right node, the next pointer should be set to `None`.

Initially, all next pointers are set to `None`. Return the root of the modified tree.

Note that the `build_tree()` function included at the top of this page will work with this problem so long as you use the updated `TreeNode()` class provided below. The `print_tree()` function needs to be modified. A modified version that prints a list of tuples where each tuple has the form `(node.val, node.next.val)` is provided below. 

```python
class TreeNode():
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# For testing
def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            if node.next is not None:
                result.append((node.val, node.next.val))
            else:
                result.append((node.val, None))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def connect(root):
    pass
```

Example Usage:

![Example Input Tree and Tree with Next Pointers Shown](../../Unit%20Assets/populating_next_right_pointers_ex1.png)

```python
values = [1, 2, 3, 4, 5, 6, 7]

root = build_tree(values)
print_tree(connect(root))
```

Example Output:

```markdown
[(1, None), (2, 3), (3, None), (4, 5), (5, 6), (6, 7), (7, None)]
```
