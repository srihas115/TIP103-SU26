class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def remove_species(ecosystem, name):
    pass

"""
                Dugong
             /         \
       Brain Coral   Lionfish
              \       /       \
         Clownfish Giant Clam  Seagrass
"""
# Use build_tree() function at top of page
values = ["Dugong", "Brain Coral", "Lionfish", None, "Clownfish", "Giant Clam", "Seagrass"]
ecosystem = build_tree(ecosystem)

# Using print_tree() function at top of page
print_tree(remove_species(ecosystem, "Lionfish"))
