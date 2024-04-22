# Matriz identidad
def eye(n):
    return [[1 if j == i else 0 for j in range(n)] for i in range(n)]


def transpose(A):
    n = len(A)
    m = len(A[0])

    B = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            B[j][i] = A[i][j]
    return B


def prod(n, A):
    sum = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            sum += n * A[i][j]
    return sum


def exp_bin_M(M: list[list], e: int):
    if e == 0:
        return eye(len(M))
    res = exp_bin_M(M, e // 2)
    res = prod(res, res)
    if e % 2:
        return prod(res, M)
    return res


print(exp_bin_M([[1, 2, 3], [4, 5, 6]], 2))
