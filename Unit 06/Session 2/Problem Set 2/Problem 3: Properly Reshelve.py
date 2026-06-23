class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def swap_books(shelf, k):
	pass

shelf = Node('Book 1', Node('Book 2', Node('Book 3', Node('Book 4', Node('Book 5')))))

print_linked_list(swap_books(shelf, 2))
