def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i < n:
        if n % i == 0:
            return False
        i += 1
    return True


# i: [1, n]
def primeros_primos(n):
    i = 0
    a = 0
    res = []

    while a < n:
        if es_primo(i):
            res.append(i)
            a += 1
        i += 1
    return res
