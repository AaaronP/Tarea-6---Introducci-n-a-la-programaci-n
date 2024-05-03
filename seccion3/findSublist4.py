def findSublist(arr, i, j):
    res = []
    for k in range(i,j+1):
        res.append(arr[k])
    return res
