class Player:
    def __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
    # ... methods from previous problems

def print_results(race_results):
    pass

peach = Player("Peach", "Daytripper")
mario = Player("Mario", "Standard Kart M")
luigi = Player("Luigi", "Super Blooper")
race_one = [peach, mario, luigi]

print_results(race_one)
