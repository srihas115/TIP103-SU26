"""
# Example 1

# Input: root = CoralKing
# Expected Output: True

# Example 2

    CoralQueen
     /      \
 CoralX    CoralX
  /  \      /  \
CoralY CoralZ CoralY CoralZ

# Input: root = CoralQueen
# Expected Output: False
"""

class TreeNode:
    def __init__(self, value, left=None):
        self.val = value
        self.left = left
        self.right = right

def is_symmetric(root):
    pass

"""
        A
      /   \
     B     B
    / \   / \
   C  D   D  C
"""
coral1 = TreeNode('A', 
                  TreeNode('B', TreeNode('C'), TreeNode('D')), 
                          TreeNode('B', TreeNode('D'), TreeNode('C')))

"""
        A
      /   \
     B     B
    / \   / \
   C  D   C  D
"""
coral2 = TreeNode('A', 
                  TreeNode('B', TreeNode('C'), TreeNode('D')), 
                          TreeNode('B', TreeNode('C'), TreeNode('D')))

print(is_symmetric(coral1))
print(is_symmetric(coral2))
