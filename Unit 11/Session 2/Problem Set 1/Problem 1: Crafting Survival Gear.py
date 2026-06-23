def craftable_gear(gear, components, supplies):
    pass

gear_1 = ["weapon"]
components_1 = [["metal", "wood"]]
supplies_1 = ["metal", "wood", "rope"]

gear_2 = ["weapon", "trap"]
components_2 = [["metal", "wood"], ["weapon", "wire"]]
supplies_2 = ["metal", "wood", "wire"]

gear_3 = ["weapon", "trap", "shelter"]
components_3 = [["metal", "wood"], ["weapon", "wire"], ["trap", "wood", "metal"]]
supplies_3 = ["metal", "wood", "wire"]

print(craftable_gear(gear_1, components_1, supplies_1))
print(craftable_gear(gear_2, components_2, supplies_2))
print(craftable_gear(gear_3, components_3, supplies_3))
