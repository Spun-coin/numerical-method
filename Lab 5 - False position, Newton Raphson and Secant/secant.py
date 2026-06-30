import numpy as np
import matplotlib.pyplot as plt
import sys

def f(x):
    return x*np.sin(x) + np.cos(x)


a=int(input("Enter a: "))
b=int(input("Enter b: "))
d=int(input("Enter the required decimal correctness: "))
tol = 5 * 10 ** (-d)

def Secant(f,a,b,tol):
    count = 1
    while True:
        if abs(f(b)-f(a))<tol:
            return None
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        a=b
        b=c
        if count > 100:
            print("ERROR :: Oscillation")
        count+=1

        if abs(f(b))<tol:
            return c, count

root,step=Secant(f,a,b,tol)
if root is None:
    print("No solution")

print(f"Root: {root:.{d+1}f}")
print(f"Step: {step}")

xvals=np.linspace(-10+root,10+root,101)
yvals=f(xvals)
plt.figure()
plt.scatter(root,f(root),marker="x",color="Black",label=f"({root:.{d+1}f},0)")
plt.plot(xvals,yvals,label="f(x) = xsin(x) + cos(x)",color="black")
plt.axvline(root)
plt.axhline(0)
plt.legend(loc="upper left")
plt.grid()
plt.title("Secant method with visualization")
plt.show()
