def find_balanced_subsequence(art_pieces):
    # [1,3,2,2,5,2,3,7] => {1: 1; 3: 2, 2: 3, 5: 1, 7: 1} => Sort by key, ascending order => {1: 1; 2: 3, 3: 2, 5: 1, 7: 1}
    # A subsequence can only contain elements equal to n (minimum) and n+1 (maximum)
    # Iterate through pairs of adjacent key values in the sorted dict => Check if they differ by 1, if true
    # Smaller key - n - is the minimum of our hypo subsequence, larger - n+1 - is the maximum
    # Add the frequency of n and n+1 to form the hypo subsequence's length, then compare with the max so far (initialized at 0)
    # Compare and update => return the max value
    # 1 and 2 => Adjacent keys => curr max = 1 + 3 = 4 > 0 => max = 4
    # 2 and 3 => Adjacent => curr max = 3 + 2 = 5 > 4 => max = 5
    # 3 and 5 => Not adjacent => Move on
    # 5 and 7 => Not adjacent => Move on => Finished traversing the dict => Return max = 5 (done)
    
    # counts = {} # the frequency map
    length = 0
    # (1:1)
    # (2:3)
    # (3:2)
    
    tally = dict()

    # Tallying (basically a freq map)
    for piece in art_pieces:
        if piece not in tally:
            tally[piece] = 1
        else:
            tally[piece] += 1

    # Sort dict
    sorted_dict = dict(sorted(tally.items()))
    print(sorted_dict)

    key_list = list(sorted_dict.keys())
    print(key_list)

    maximum = 0
    for i in range(0,len(key_list)-2):
        if key_list[i+1]-key_list[i] == 1:
            # Update max
            length = tally[key_list[i]] + tally[key_list[i+1]]
            if length > maximum:
                maximum = length

    return maximum


art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))