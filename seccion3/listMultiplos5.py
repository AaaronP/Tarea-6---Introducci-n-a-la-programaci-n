def multiplosList(arr, n):
    c = 0
    for i in range(len(arr)):
        if n % arr[i] == 0:
            c += 1

    return c
