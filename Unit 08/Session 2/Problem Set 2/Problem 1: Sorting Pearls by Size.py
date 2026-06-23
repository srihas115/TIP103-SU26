class Pearl:
    def __init__(self, size, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

def smallest_to_largest_recursive(pearls):
    sorted_list = []

    def inorder_traversal(node):
        if node:
            inorder_traversal(node.left)
            sorted_list.append(node.val)
            inorder_traversal(node.right)

    inorder_traversal(pearls)
    return sorted_list

def smallest_to_largest_iterative(pearls):
    pass

"""
        3
       / \
      /   \
     1     5
      \   / \
       2 4   8
"""

#  Using build_tree() from the top of the page
values = [3, 1, 5, None, 2, 4, 8]
pearls = build_tree(values)

print(smallest_to_largest_recursive(pearls))
print(smallest_to_largest_iterative(pearls))
