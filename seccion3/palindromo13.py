def palindromo(arr):
    s = len(arr) - 1

    for i in range(len(arr)):
        if arr[i] != arr[s]:
            return False
        s -= 1
    return True
