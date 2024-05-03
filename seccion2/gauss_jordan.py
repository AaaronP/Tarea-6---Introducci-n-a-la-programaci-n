def gauss_jordan(A, b):
    n = len(A)

    aux_m = []
    for i in range(n):
        row = A[i] + [b[i]]
        aux_m.append(row)

    for i in range(n):
        fil = aux_m[i]
        pivot = fil[i]

        if pivot != 0:
            fil = [element // pivot for element in fil]
            aux_m[i] = fil

        for j in range(i + 1, n):
            cero = aux_m[j][i]
            for k in range(i, n + 1):
                aux_m[j][k] -= cero * aux_m[i][k]

    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            cero = aux_m[j][i]
            for k in range(n, -1, -1):
                aux_m[j][k] -= cero * aux_m[i][k]

    res = [row[-1] for row in aux_m]

    return tuple(res)


values = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
results = [8, -11, -3]

print(gauss_jordan(values, results))  # (-2, 5, -6)
