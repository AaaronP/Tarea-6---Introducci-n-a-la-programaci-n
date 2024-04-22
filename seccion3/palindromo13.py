def invertir_aux(arr, i, s):
    if i >= s:
        return arr
    
    arr[i] ^= arr[s]
    arr[s] ^= arr[i]
    arr[i] ^= arr[s]

    return invertir_aux(arr, i+1, s-1)

def invertir(arr):
    return invertir_aux(arr, 0, len(arr)-1)

def palindromo(arr):
    print(arr)
    newArr = arr
    print(newArr)
    invertido = invertir(newArr)
    print(newArr, arr, invertido)
    for i in range(len(arr)):
        if arr[i] != invertido[i]:
            return False
    return True

print(palindromo([1,2,3,4,5]))