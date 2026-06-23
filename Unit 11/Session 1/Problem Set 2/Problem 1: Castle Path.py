def path_to_castle(kingdom, town, castle):
    pass

grid = [
    ['X', 'O', 'X', 'X', 'O'], # Row 'O'
    ['X', 'X', 'X', 'X', 'O'], # Row 1
    ['O', 'O', 'X', 'X', 'O'], # Row 2
    ['X', 'O', 'X', 'X', 'X']  # Row 3
]

castle = (3, 4)

town_1 = (0, 0)
town_2 = (0, 4)
town_3 = (3, 0)

print(path_to_castle(town_1, grid, castle))
print(path_to_castle(town_2, grid, castle))
print(path_to_castle(town_3, grid, castle))
