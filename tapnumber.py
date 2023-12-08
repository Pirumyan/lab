def tap(matrix: list) -> list:
    res = []
    syunner, toxer = len(matrix), len(matrix[0])

    for i in range(syunner):
        for j in range(toxer):
            element = matrix[i][j]
            if element == min(matrix[i]) and element == max(matrix[k][j] for k in range(syunner)):
                res.append((i, j, element))

    return res if len(res) > 0 else None



matrix = [[3, 1, 4],
          [5, 2, 6],
          [9, 7, 8]]

print(tap(matrix))
