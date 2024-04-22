def min(list):
    minN = list[0]
    index = 0

    for i in range(len(list)):
        if list[i] < minN:
            minN = list[i]
            index = i
    return (minN, index)
