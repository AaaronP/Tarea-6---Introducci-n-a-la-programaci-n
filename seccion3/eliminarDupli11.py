def duplicados(arr):
    res = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] != arr[j]:
                res.append(arr[i])
    return res


print(duplicados([1, 1, 1, 1, 1, 1, 2, 3, 4, 5]))
