def reemplazar(a, b, arr):
    for i in range(len(arr)):
        if arr[i] == a:
            arr[i] = b
    return arr
