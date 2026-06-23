def walls_and_gates(castle):
    pass

castle = [
    [float('inf'), -1, 0, float('inf')],            # Row 0
    [float('inf'), float('inf'), float('inf'), -1], # Row 1
    [float('inf'), -1, float('inf'), -1],           # Row 2
    [0, -1, float('inf'), float('inf')]             # Row 3
    ]

print(walls_and_gates(castle))
