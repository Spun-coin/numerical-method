import numpy as np
import matplotlib.pyplot as plt
import sys

def f(x):
    return x*np.sin(x) + np.cos(x)

def false_position(f,a,b,tol):
    if f(a)*f(b)>0:
        print("Not good value")
        sys.exit(0)
    while True:
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        

        if f(a)*f(c)<0:
            b=c
        else:
            a=c
        if abs(f(c))<tol:
            return c, f(c)

a,b=12,13
d=int(input("Enter the required correctness: "))
tol=5*10**(-d)
root,fval=false_position(f,a,b,tol)
print(f"Root: {root:.{d+1}f}")

xvals=np.linspace(-10+root,10+root,101)
yvals=f(xvals)
plt.figure()
plt.scatter(root,f(root),marker="x",color="Black",label=f"({root:.{d+1}f},0)")
plt.plot(xvals,yvals,label="f(x) = xsin(x) + cos(x)")
plt.axvline(root)
plt.axhline(0)
plt.legend(loc="upper left")
plt.grid()
plt.title("False position method with visualization")
plt.show()
