class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def is_symmetric(head):
	pass

head1 = Node("Bitterling", Node("Crawfish", Node("Bitterling")))
head2 = Node("Bitterling", Node("Carp", Node("Koi")))

print(is_symmetric(head1))
print(is_symmetric(head2))
