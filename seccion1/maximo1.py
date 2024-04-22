def max(list):
    maxN = list[0]
    index = 0

    for i in range(len(list)):
        if list[i] > maxN:
            maxN = list[i]
            index = i
    return (maxN, index)
