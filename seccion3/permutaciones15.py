def generar_permutaciones(list):
    if len(list) == 1:
        return [list]

    permutaciones = []

    for i in range(len(list)):
        el_actual = list[i]
        sublistas = list[:i] + list[i + 1 :]
        perm_sublista = generar_permutaciones(sublistas)

        for perm in perm_sublista:
            permutaciones.append([el_actual] + perm)

    return permutaciones
