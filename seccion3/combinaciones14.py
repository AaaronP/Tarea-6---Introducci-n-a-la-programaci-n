def combinaciones(lista, n):
    if n == 0:
        return [[]]
    if len(lista) < n:
        return []

    aux = []
    for i in range(len(lista)):
        primero = lista[i]
        res = lista[i + 1 :]
        for j in combinaciones(res, n - 1):
            aux.append([primero] + j)
    return aux
