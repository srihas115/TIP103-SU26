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

def game_result(head):
    pass

game1 = Node(2, Node(1))
game2 = Node(2, Node(5, Node(4, Node(7, Node(20, Node(5))))))
game3 = Node(4, Node(5, Node(2, Node(1))))

print(game_result(game1))
print(game_result(game2))
