import numpy as np
n=int(input("Enter n values: "))
A=np.zeros((n,n+1),dtype=float)
for i in range(n):
    rowstr=input(f"Row {i+1}: ")
    rowval=list(map(float,rowstr.split()))
    if len(rowval) != n+1:
        raise Exception ("Mistake in inserting values")
    A[i,:]=rowval
print(A)
d=int(input("Enter the required decimal correctness: "))
tol = 5 * 10 ** (-d-1)
for j in range(n):
    if abs(A[j][j])<tol:
        raise Exception("Diagonal value is zero")
    for i in range(n):
        if i!=j:
            ratio=A[i][j]/A[j][j]
            for k in range(n+1):
                A[i][k]=A[i][k]-ratio*A[j][k]
print("Final solution: ")
for i in range(n):
    x=A[i][n]/A[i][i]
    print(np.round(x,d))