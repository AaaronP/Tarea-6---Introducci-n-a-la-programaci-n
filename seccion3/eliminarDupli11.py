def repetidos(lista):
    checked = []
    res = []

    for i in lista:
        if i not in checked:
            checked.append(i)
            res.append(i)
    return res