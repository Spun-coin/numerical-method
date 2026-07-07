import numpy as np
def f(x):
    return np.array([x[0]**5-x[1]**3-10,x[0]**3+x[1]**5-30])
def J(x):
    return np.array([[5*x[0]**4,-3*x[1]**2],[3*x[0]**2,5*x[1]**4]])

for i in range(1):
    rowstr=input(f"Enter the initial guesses: ")
    x=list(map(float,rowstr.split()))

d=int(input("Enter the required decimal correctness: "))
tol = 5 * 10 ** (-d-1)
i=1
while True:
    h=np.linalg.solve(J(x),-f(x))
    x=x+h
    error=max(abs(h))
    #print(h)
    print(f"step:{i}, {x}")
    i+=1
    if i>100:
        print("There is no soultion for the given initial values")
        exit(0)
    if error<tol:
        break

print("Final solution:")
print(np.round(x,d))