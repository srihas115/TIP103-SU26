def bacon_number(bacon_network, celeb):
    pass

bacon_network = {
    "Kevin Bacon": ["Kyra Sedgewick", "Forest Whitaker", "Julia Roberts", "Tom Cruise"],
    "Kyra Sedgewick": ["Kevin Bacon", "Tom Cruise"],
    "Tom Cruise": ["Kevin Bacon", "Kyra Sedgewick"],
    "Forest Whitaker": ["Kevin Bacon", "Denzel Washington"],
    "Denzel Washington": ["Forest Whitaker", "Julia Roberts"],
    "Julia Roberts": ["Denzel Washington", "Kevin Bacon", "George Clooney"],
    "George Clooney": ["Julia Roberts", "Vera Farmiga"],
    "Vera Farmiga": ["George Clooney", "Max Theriot"],
    "Max Theriot": ["Vera Farmiga", "Jennifer Lawrence"],
    "Jennifer Lawrence": ["Max Theriot"]
}

print(bacon_number(bacon_network, "Jennifer Lawrence"))
print(bacon_number(bacon_network, "Tom Cruise"))
