# Problem 8: Distributing Sunken Treasure

You and your friends have found a ship wreck full of gold pieces as part of a shipwreck and want to distribute the gold evenly amongst yourselves as efficiently as possible. 

You are given the `root` of a binary tree with `n` nodes representing you and your friends where each friend currently has `node.val` coins. There are `n` coins in the whole tree (one for each of you!).

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity. 

```python
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def distribute_coins(root):
    pass
```

Example Usage:

Example 1:
!['root1' tree with movement of coins shown](../../Unit%20Assets/distributing_sunken_treasure_ex1.png)

Example 2:
!['root2' tree with movement of coins shown](../../Unit%20Assets/distributing_sunken_treasure_ex2.png)

```python
"""
    3
   / \
  0   0
"""
root1 = TreeNode(3, TreeNode(0), TreeNode(0))

"""
    0
   / \
  3   0
"""
root2 = TreeNode(0, TreeNode(3), TreeNode(0))

print(distribute_coins(root1))
print(distribute_coins(root2))
```

Example Output:

```markdown
2
Example 1 Explanation: From the root of the tree, we move one coin to its left child, 
and one coin to its right child.

3
Example 1 Explanation: From the left child of the root, we move two coins to the root 
[taking two moves]. Then, we move one coin from the root of the tree to the right child.
```

<details>
  <summary><strong>💡 Hint: Choosing a Traversal Order</strong></summary>

Oftentimes when we solve a binary tree problem, the traversal order doesn't matter. But sometimes, it can help to specifically follow a preorder, inorder, or postorder traversal. This problem would most benefit from a postorder traversal because postorder processes each subtree starting from the leaves and works its way up to the root. This is necessary because we want to know how many extra or deficient coins each subtree has before balancing the parent node.

Using a postorder approach, by the time we process a parent node, the coins in its children’s subtrees will already been balanced, allowing us to decide how many coins should move between the parent and its children.

</details>

<br>
