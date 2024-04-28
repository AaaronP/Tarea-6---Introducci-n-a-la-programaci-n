def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def transpuesta(M):
    b = [[0 for _ in range(len(M))] for _ in range(len(M[0]))]

    for i in range(len(M)):
        for j in range(len(M[0])):
            b[j][i] = M[i][j]
    return b


def prod_punto(A, B):
    sum = 0
    for i in range(len(A)):
        sum += A[i] * B[i]
    return sum


def prod(A, B):
    t_b = transpuesta(B)
    return [[prod_punto(fil, col) for col in t_b] for fil in A]


def exp_bin(M, n):
    if n == 0:
        return eye(len(M))

    res = exp_bin(M, n // 2)
    res = prod(res, res)

    if n % 2:
        return prod(res, M)
    return res
