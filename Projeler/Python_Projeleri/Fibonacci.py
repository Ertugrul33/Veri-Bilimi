def fibonacci(x):
    A = [0,1]
    for i in range(1,x-1):
        A.append(A[i]+A[i-1])
    return A