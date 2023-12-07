def mta_simetrik(mat):
    matTranspos = [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]
    return matTranspos == mat


# mat = [[1,2,3],[2, 4, 5], [3,5,8]]
# print(mta_simetrik(mat))


def det():
    mat = [[2, 4],
           [3, 5]]
    return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])


def mat_gumar():
    mat1 = [[1, 2, 3], [2, 4, 5], [3, 5, 8]]
    mat2 = [[1, 2, 2], [2, 4, 5], [3, 5, 8]]
    new_mat = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1))] for i in range(len(mat1[0]))]
    return new_mat


def artadryal():
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat2 = [[2, 3, 4], [5, 6, 7], [1, 2, 4]]
    new_mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    summ = 0

    for i in range(len(mat1)):
        for j in range(len(mat1)):
            for k in range(len(mat1)):
                summ += mat1[i][k] * mat2[k][j]
            new_mat[i][j] = summ
            summ = 0

    print(new_mat)


def mat_mogakan():
    mat = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    magic = sum(mat[0])

    glxavor = sum(mat[i][i] for i in range(len(mat)))
    ojandak = sum(mat[i][-1-i] for i in range((len(mat))))
    if magic != glxavor != ojandak:
        return False
    for i in range(1, len(mat)):
        if magic != sum(mat[i]):
            return False
    for j in range(len(mat)):
        if sum(mat[i][j] for i in range(len(mat))) != magic:
            return False
    return True


def tmbayin_ket(mat):
    tmbayin = []
    transposed_mat = [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            value = mat[i][j]
            if value == min(transposed_mat[j]) and value == max(mat[i]):
                tmbayin.append(value)

    return tmbayin

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(tmbayin_ket(mat))

