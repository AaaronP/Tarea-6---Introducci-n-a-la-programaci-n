def exp_conjunto(list, n):
    if n == 0:
        return [[]]

    aux = []
    for i in list:
        for j in exp_conjunto(list, n - 1):
            aux.append([i] + j)
    return aux


print(exp_conjunto([1, 2], 2))
