class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_length(protein):
    pass

protein_head = Node('Ala', Node('Gly', Node('Leu', Node('Val'))))
protein_head.next.next.next.next = protein_head.next

print(cycle_length(protein_head))
