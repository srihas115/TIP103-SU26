def eventual_safe_locations(city):
    pass

city_1 = [
    [1,2], # Location 0
    [2,3], # Location 1
    [5],   # Location 2
    [0],   # Location 3
    [5],   # Location 4
    [],    # Location 5
    []     # Location 6
    ]

city_2 = [
    [1,2,3,4], # Location 0
    [1,2],     # Location 1
    [3,4],     # Location 2
    [0,4],     # Location 3
    []         # Location 4
    ]

print(eventual_safe_locations(city_1))
print(eventual_safe_locations(city_2))
