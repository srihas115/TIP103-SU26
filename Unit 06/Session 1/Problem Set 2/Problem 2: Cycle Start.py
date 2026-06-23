class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_start(path_start):
    pass

path_start = Node('Start', Node('Point 1', Node('Point 2', Node('Point 3'))))
path_start.next.next.next.next = path_start.next
print(cycle_start(path_start))
