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

def next_highest_scoring_contestant(contestant_scores):
    pass

contestant_scores1 = Node(2, Node(1, Node(5)))
contestant_scores2 = Node(2, Node(7, Node(4, Node(3, Node(5)))))

print(next_highest_scoring_contestant(contestant_scores1))
print(next_highest_scoring_contestant(contestant_scores2))
