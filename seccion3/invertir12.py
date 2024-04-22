def invertir_aux(arr, i, s):
    if i >= s:
        return arr
    
    arr[i] ^= arr[s]
    arr[s] ^= arr[i]
    arr[i] ^= arr[s]

    return invertir_aux(arr, i+1, s-1)

def invertir(arr):
    return invertir_aux(arr, 0, len(arr)-1)