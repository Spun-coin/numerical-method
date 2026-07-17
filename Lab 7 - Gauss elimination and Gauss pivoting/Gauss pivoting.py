import numpy as np

n = int(input("Enter the value of n: "))
A = np.zeros((n, n+1), dtype=float)

for i in range(n):
    rowstr = input(f"Row:{i+1}: ")
    rowvals = list(map(float, rowstr.split()))
    A[i, :] = rowvals

tol = 0.0001

for i in range(n-1):
    pivot = i
    # Find the largest element in the current column
    for j in range(i+1, n):
        if abs(A[j][i]) > abs(A[pivot][i]):
            pivot = j
            
    # Check if the largest pivot found is too close to zero
    if abs(A[pivot][i]) < tol:
        raise Exception("Diagonal error: Matrix is singular or nearly singular.")
        
    # Swap the rows if a better pivot row was found
    if pivot != i:
        A[[i, pivot]] = A[[pivot, i]]  # Correct way to swap rows in NumPy

# --- GAUSSIAN ELIMINATION ---
for j in range(n-1):
    if abs(A[j][j]) < tol:
        raise Exception("Diagonal error")
    for i in range(j+1, n):
        ratio = A[i][j] / A[j][j]
        for k in range(j, n+1):
            A[i][k] = A[i][k] - ratio * A[j][k]

print("\nUpper Triangular Matrix:")
for i in range(n):
    print(A[i])

# --- BACK SUBSTITUTION ---
x = np.zeros((n), dtype=float)
for i in range(n-1, -1, -1):
    current_sum = 0
    for j in range(i+1, n):
        current_sum += A[i][j] * x[j]  
    x[i] = (A[i][n] - current_sum) / A[i][i]

print("\nSolution Vector x:")
print(x)