def sum(v, w, n):
    return sum_aux(v, w, 0, n, 0)


def sum_aux(v, w, i, n, res):
    if i > n:
        return res

    res += (v[i] - w[i]) * (v[i] - w[i])
    return sum_aux(v, w, i + 1, n, res)


def sqrt2_aux(i, s, n, p):
    m = (i + s) // 2

    if m * m - p < n and m * m + p > n:
        return m

    if m * m > n:
        return sqrt2_aux(i, m, n, p)
    return sqrt2_aux(m, s, n, p)


def sqrt2(n):
    return sqrt2_aux(1, n, n, 1e-6)


# La longitud de ambos deben ser iguales
def distancia(v, w):
    return sqrt2(sum(v, w, len(v) - 1))
