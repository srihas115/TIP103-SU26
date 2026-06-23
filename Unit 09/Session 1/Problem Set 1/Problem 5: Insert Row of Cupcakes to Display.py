class TreeNode():
    def __init__(self, sweetness, left=None, right=None):
        self.val = sweetness
        self.left = left
        self.right = right

def insert_row(display, flavor, depth):
    pass

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Red Velvet
"""
# Using build_tree() function included at top of page
cupcake_flavors = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Red Velvet"]
display = build_tree(cupcake_flavors)

# Using print_tree() function included at top of page
print_tree(insert_row(display, "Mocha", 3))
