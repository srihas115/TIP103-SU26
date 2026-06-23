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

def similar_book_count(all_books, subset):
	pass

all_books1 = Node(0, Node(1, Node(2, Node(3))))
subset1 = [0, 1, 3]

all_books2 = Node(0, Node(1, Node(2, Node(3, Node(4)))))
subset2 = [0, 3, 1, 4]

print(similar_book_count(all_books1, subset1))
print(similar_book_count(all_books2, subset2))
