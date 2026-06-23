def find_kingdom_lineage(names, relationships):
    pass

names_1 = ["Henry", "Elizabeth", "George", "Mary", "Charles", "William"]
relationships_1 = [["Henry", "Mary"], ["Elizabeth", "Mary"], ["George", "Mary"], ["Charles", "William"], ["William", "Mary"]]

names_2 = ["Alice", "Bob", "Catherine", "Diana", "Edward"]
relationships_2 = [["Alice", "Bob"], ["Alice", "Catherine"], ["Bob", "Diana"], ["Catherine", "Diana"], ["Diana", "Edward"]]

print(find_kingdom_lineage(names_1, relationships_1))
print(find_kingdom_lineage(names_2, relationships_2))
