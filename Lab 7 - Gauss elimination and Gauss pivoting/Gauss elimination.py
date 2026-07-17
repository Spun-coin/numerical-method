import numpy as np

n = int(input("Enter the value of n: "))
A = np.zeros((n, n+1), dtype=float)

for i in range(n):
    rowstr = input(f"Row:{i+1}: ")
    rowvals = list(map(float, rowstr.split()))
    A[i, :] = rowvals

tol = 0.0001
for j in range(n-1):
    if abs(A[j][j]) < tol:
        raise Exception("Diagonal error")
    for i in range(j+1, n):
        if i != j:
            ratio = A[i][j] / A[j][j]
            for k in range(j, n+1):
                A[i][k] = A[i][k] - ratio * A[j][k]

print("\nUpper Triangular Matrix:")
for i in range(n):
    print(A[i])

x = np.zeros((n), dtype=float)
for i in range(n-1, -1, -1):
    sum = 0
    for j in range(i+1, n):
        sum += A[i][j] * x[j]  
    x[i] = (A[i][n] - sum) / A[i][i]

print("\nSolution Vector x:")
print(x)