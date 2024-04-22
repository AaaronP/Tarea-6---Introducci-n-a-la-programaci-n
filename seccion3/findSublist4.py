def rangeSublist(arr, i, j):
    sublists = []
    for k in range(i, j):
        if type(arr[k]) == list:
            sublists.append(arr[k])
    return sublists
