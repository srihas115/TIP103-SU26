def find_max_star_power(collaboration_map, start, target, budget):
    pass

collaboration_map = {
    "Leonardo DiCaprio": [("Brad Pitt", 40, 300), ("Robert De Niro", 30, 200)],
    "Brad Pitt": [("Leonardo DiCaprio", 40, 300), ("Scarlett Johansson", 20, 150)],
    "Robert De Niro": [("Leonardo DiCaprio", 30, 200), ("Chris Hemsworth", 50, 350)],
    "Scarlett Johansson": [("Brad Pitt", 20, 150), ("Chris Hemsworth", 30, 250)],
    "Chris Hemsworth": [("Robert De Niro", 50, 350), ("Scarlett Johansson", 30, 250)]
}

print(find_max_star_power(collaboration_map, "Leonardo DiCaprio", "Chris Hemsworth", 600))
