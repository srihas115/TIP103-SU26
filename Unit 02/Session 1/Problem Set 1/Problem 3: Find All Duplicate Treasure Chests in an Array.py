def find_duplicate_chests(chests):
    hashmap = {}
    output = []
    for i in chests:
        hashmap[i] = hashmap.get(i, 0) + 1

    for key, value in hashmap.items():
        if value >= 2:
            output.append(key)
    
    return output

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))