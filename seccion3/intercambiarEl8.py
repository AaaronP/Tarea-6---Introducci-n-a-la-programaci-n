def intercambiar(a, b, arr):
    arr[a] ^= arr[b]
    arr[b] ^= arr[a]
    arr[a] ^= arr[b]

    return arr
