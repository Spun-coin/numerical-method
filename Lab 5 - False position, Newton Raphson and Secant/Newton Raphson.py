import numpy as np
import matplotlib.pyplot as plt
import sys

def f(x):
    return x*np.sin(x) + np.cos(x)

def g(x): #derivative of f(x)
    return x*np.cos(x)

x0=int(input("Enter x0: "))
d=int(input("Enter the required decimal correctness: "))
tol = 5 * 10 ** (-d)
def Newton_Raphson(f,g,x0,tol):
    count = 1
    while True:
        if abs(g(x0))<tol:
            return None
        x1=x0-f(x0)/g(x0)
        x0=x1
        if count>100:
            print("ERROR :: OSCILLATION")
        count+=1

        if abs(f(x0))<tol:
            return x0,count

root,step=Newton_Raphson(f,g,x0,tol)
if root is None:
    print("No solution")

print(f"Root: {root:.{d+1}f}")
print(f"Step: {step}")

xvals=np.linspace(-10+root,10+root,101)
yvals=f(xvals)
plt.figure()
plt.scatter(root,f(root),marker="x",color="Black",label=f"({root:.{d+1}f},0)")
plt.plot(xvals,yvals,label="f(x) = xsin(x) + cos(x)")
plt.axvline(root)
plt.axhline(0)
plt.legend(loc="upper left")
plt.grid()
plt.title("Newton-Raphson method with visualization")
plt.show()
