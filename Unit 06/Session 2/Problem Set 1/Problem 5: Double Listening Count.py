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

def double_listeners(monthly_listeners):
    pass

monthly_listeners1 = Node(1, Node(8, Node(9))) # 189
monthly_listeners2 = Node(9, Node(9, Node(9))) # 999

print_linked_list(double_listeners(monthly_listeners1))
print_linked_list(double_listeners(monthly_listeners2))
