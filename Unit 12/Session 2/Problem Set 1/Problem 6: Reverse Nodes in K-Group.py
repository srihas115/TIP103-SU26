class Node():
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next

def reverse_k_group(head, k):
    pass

list_1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))

# Using print_linked_list() function included at top of page
print_linked_list(reverse_k_group(list_1, 2))

list_2 = Node(1, Node(2, Node(3, Node(4, Node(5)))))

# Using print_linked_list() function included at top of page
print_linked_list(reverse_k_group(list_2, 3))
