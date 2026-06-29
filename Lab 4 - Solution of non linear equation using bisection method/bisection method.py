import numpy as np
import matplotlib.pyplot as plt
import sys 
def f(x):
    return 4*np.log(x)

def bisection(f,a,b,tolerance):
    if f(a)*f(b)>0:
        print("Not good guess")
        sys.exit(0)
    while True:
        c=(a+b)/2
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
        if abs(f(c))<tolerance:
            return c, f(c)

a, b = 0,2
d=int(input("Enter the required decimal correctness: "))
tolerance = 5 * 10 ** (-d)
root,fval=bisection(f,a,b,tolerance)

print(f"Root: {root:.{d+1}f}")

xvals = np.linspace(-10+root, 10+root, 200)
yvals=f(xvals)
plt.figure()
plt.scatter(root,f(root),marker="x",color="black",label=f"root = {root:.{d+1}f}")
plt.plot(xvals,yvals,label="f(x) = 4sin(x+2)")
plt.axhline(0,color="black")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.axvline(root,color="black")
plt.legend(loc="upper left")
plt.grid()
plt.title("Bisection method with visualization")
plt.show()