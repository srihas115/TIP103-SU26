def can_make_balanced(code):
    # code.sort()
    # foundExtra = False
    hashmap = {}
    
    for c in code:
        hashmap[c] = hashmap.get(c, 0) + 1  
    
    for key in hashmap.keys():
        hashmap[key] -= 1
        
        count = set()
        for value in hashmap.values():
            if value != 0:
                count.add(value)
            
        if len(count) == 1:
            return True
        
        hashmap[key] += 1

    return False
        
        
def can_make_balanced2(code):
    code = sorted(code)
    code = "".join(code)
    curr = 0
    counts = {}
    
    for i, c in enumerate(code):
        # curr += 1
        # ERROR^

        # ERROR: it was c != 0, it should be i != 0. c is a char, i is an index
        if i != 0 and code[i - 1] != code[i]:
            counts[curr] = counts.get(curr, 0) + 1
            curr = 0
            
        curr += 1
        # ^ ERROR Fixed: off by one, we were incrementing too early
        
        if len(counts) > 2:
            return False
        
    counts[curr] = counts.get(curr, 0) + 1
    
    # print(counts)
    
    if len(counts) == 1:
        return False

    first = list(counts.items())[0]
    second = list(counts.items())[1]

    if first[0] > second[0]:
        first, second = second, first
    
    if first[1] == 1: # one additional letter that can be removed to balance
        return True
    
    if second[0] - first[0] == 1 and second[1] == 1: # greater count has exactly one more than the rest
        return True

    return False
        
    
code1 = "arghh"
code2 = "haha"
code3 = "aabbccdddee"

print("O(n) way: ")
print(can_make_balanced(code1))
print(can_make_balanced(code2))
print(can_make_balanced(code3))

print()

print("O(nlogn) way: ")
print(can_make_balanced2(code1))
print(can_make_balanced2(code2))
print(can_make_balanced2(code3))