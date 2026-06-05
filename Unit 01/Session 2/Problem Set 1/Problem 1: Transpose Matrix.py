def transpose(matrix):
    res = []
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(cols):
        currRow = []
        for j in range(rows):
            currRow.append(matrix[j][i])
        res.append(currRow)
    
    
    print(res)
    

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix)