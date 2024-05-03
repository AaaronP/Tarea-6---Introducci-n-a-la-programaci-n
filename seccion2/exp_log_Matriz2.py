def prod_punto(a, b):
    p = 0
    for i in range(len(a)):
        p += a[i] * b[i]
    return p


def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def prodMat(A, B):
    Bt = transpose(B)
    return [[prod_punto(a, b) for b in Bt] for a in A]


def eye(M):
    return [[1 if i == j else 0 for j in range(len(M[0]))] for i in range(len(M))]


def exp_bin(M, n):
    if n == 0:
        return eye(M)

    res = exp_bin(M, n // 2)
    res = prodMat(res, res)

    if n % 2:
        return prodMat(res, M)
    return res
