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

def get_random(catalogue):
    pass

catalogue = Node(('Homegoing', 'Yaa Gyasi'),
                Node(('Pachinko', 'Min Jin Lee'),
                         Node(('The Night Watchman', 'Louise Erdrich'))))

print(get_random(catalogue))
