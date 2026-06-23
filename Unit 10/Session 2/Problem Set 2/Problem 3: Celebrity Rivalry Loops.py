def has_rivalry_loop(rivalries):
    pass

rivalries_1 = [
    [1],
    [0, 2],
    [1, 3],
    [2]
]

rivalries_2 = [
    [1],
    [2],
    [3],
    [0]
]

print(has_rivalry_loop(rivalries_1))
print(has_rivalry_loop(rivalries_2))
