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

def spiralize_books(m, n, new_reads):
	pass

new_reads1 = Node('Book 1', Node('Book 2', Node('Book 3', Node('Book 4', Node('Book 5', Node('Book 6',
Node('Book 7', Node('Book 8', Node('Book 9', Node('Book 10', Node('Book 11', Node('Book 12', Node('Book 13')))))))))))))
new_reads2 = Node('Book 1', Node('Book 2', Node('Book 3')))

print(spiralize_books(3, 5, new_reads1))
print(spiralize_books(1, 4, new_reads2))
