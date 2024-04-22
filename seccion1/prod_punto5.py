def prod_punto(A, B):
    return prod_aux(A, B, 0, [])


def prod_aux(A, B, i, res: list):
    if i == len(A):
        return res

    res.append(A[i] * B[i])

    return prod_aux(A, B, i + 1, res)
