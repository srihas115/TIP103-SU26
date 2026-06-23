class TreeNode:
    def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def build_cookie_tree(descriptions):
    pass

descriptions1 = [
    ["Chocolate Chip", "Peanut Butter", 1],
    ["Chocolate Chip", "Oatmeal Raisin", 0],
    ["Peanut Butter", "Sugar", 1]
]

descriptions2 = [
    ["Ginger Snap", "Snickerdoodle", 0],
    ["Ginger Snap", "Shortbread", 1]
]

# Using print_tree() function included at top of page
print_tree(build_cookie_tree(descriptions1))
print_tree(build_cookie_tree(descriptions2))
