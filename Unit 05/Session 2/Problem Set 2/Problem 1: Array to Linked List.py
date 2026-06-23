class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value.character, end=" -> " if current.next else "\n")
        current = current.next

def arr_to_ll(arr):
    pass

mario = Player("Mario", "Mushmellow")
luigi = Player("Luigi", "Standard LG")
peach = Player("Peach", "Bumble V")

print_linked_list(arr_to_ll([mario, luigi, peach]))
print_linked_list(arr_to_ll([peach]))
