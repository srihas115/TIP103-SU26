class TreeNode():
     def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def lca_youngest_children(root):
    pass

"""
                Isadora the Hexed
                /                \
            Thorne               Raven
           /      \             /      \
      Dracula     Doom      Hecate    Wraith
                 /    \
             Gloom   Mortis
"""
# Using build_tree() function included at top of the page
members = ["Isadora the Hexed", "Thorne", "Raven", "Dracula", "Doom", "Hecate", "Wraith", None, None, "Gloom", "Mortis"]
family1 = build_tree(members)

"""
              Grandmama Addams
              /              \
        Gomez Addams        Uncle Fester
                \
            Wednesday Addams
"""
members = ["Grandmama Addams", "Gomez Addams", "Uncle Fester", None, "Wednesday Addams"]
family2 = build_tree(members)

print(lca_youngest_children(family1))
print(lca_youngest_children(family2))
