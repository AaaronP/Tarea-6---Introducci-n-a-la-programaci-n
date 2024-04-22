def sum_vectores(A, B):
    sum = [0 for _ in range(len(A))]

    for i in range(len(A)):
        sum[i] = A[i] + B[i]
    return sum
