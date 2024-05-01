def permutaciones(list):
    if len(list) == 1:
        return [list]

    res = []

    for i in range(len(list)):
        el_actual = list[i]
        sublistas = list[:i] + list[i + 1 :]
        perm_sublista = permutaciones(sublistas)

        for j in perm_sublista:
            res.append([el_actual] + j)

    return res
