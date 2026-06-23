class Node:
    def __init__(self, val, next=None, random=None):
        self.value = val
        self.next = next
        self.random = random

# For testing, prints (value, random pointer value) for each node
def print_linked_list(head):
    current = head
    if not head:
        print("Empty List")
    while current:
        print((current.value, current.random.value), end=" -> " if current.next else "\n")
        current = current.next

# For testing, prints object ids for each node
def print_list_ids(head):
    current = head
    if not head:
        print("Empty List")
    while current:
        print(id(current), end=" -> " if current.next else "\n")
        current = current.next

def copy_random_list(head):
    pass

seven = Node(7)
thirteen = Node(13)
eleven = Node(11)
ten = Node(10)
one = Node(1)

seven.next = thirteen
thirteen.next = eleven
eleven.next = ten
ten.next = one

thirteen.random = seven
eleven.random = one
ten.random = eleven
one.random = seven

copied_list = copy_random_list(seven)
print_linked_list(copied_list)
print_list_ids(seven)
print_list_ids(copied_list)

one = Node(1)
two = Node(2)

one.next = two

one.random = two
two.random = two

copied_list = copy_random_list(one)
print_linked_list(copied_list)
print_list_ids(one)
print_list_ids(copied_list)

first = Node(3)
second = Node(3)
third = Node(3)

first.next = second
second.next = third

second.random = first

copied_list = copy_random_list(first)
print_linked_list(copied_list)
print_list_ids(first)
print_list_ids(copied_list)
