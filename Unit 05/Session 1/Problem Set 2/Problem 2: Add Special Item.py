class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []

    def add_item(self, item_name):
        pass

player_one = Player("Yoshi", "Dolphin Dasher")
print(player_one.items)

player_one.add_item("red shell")
print(player_one.items)

player_one.add_item("super star")
print(player_one.items)

player_one.add_item("super smash")
print(player_one.items)
