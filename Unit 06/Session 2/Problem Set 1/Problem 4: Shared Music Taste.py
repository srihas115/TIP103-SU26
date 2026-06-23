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

def playlist_overlap(playlist_a, playlist_b):
    pass

playlist_a = Node('Song A', Node('Song B'))
playlist_b = Node('Song X', Node('Song Y', Node('Song Z')))
shared_segment = Node('Song M', Node('Song N', Node('Song O')))

playlist_a.next.next = shared_segment
playlist_b.next.next.next = shared_segment

intersection = (playlist_overlap(playlist_a, playlist_b))

if intersection:
    print(intersection.value)
else:
    print(intersection)
