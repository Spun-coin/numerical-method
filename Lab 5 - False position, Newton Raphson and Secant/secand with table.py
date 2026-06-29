import numpy as np

def f(x):
    return x*np.sin(x) + np.cos(x)

def secand(f,a,b,tol):
    print("--"*30)
    print(f"| {'count':>5}|  {'a  ':>10}  |  {'b'  :>10}  |{'c'  :>10}    |")
    print("--"*30)
    count=1
    while True:
        if abs(f(b)-f(a))<tol:
            print("ERROR :: Slope Zero")
            return None
        
        c = (a*f(b) - b*f(a))/(f(b)-f(a))

        print(f"|{count:6d}|  {a: 10.6f}  |  {b: 10.6f}  |  {c: 10.6f}  |")
        #a=b
        #b=c

        if count>100:
            print("ERROR :: Oscillation")
            return None
        #count += 1
        if abs(c-b) < tol:
            print("--"*30)
            return c,f(c),count
        
        a=b
        b=c
        count +=1
        
a,b=2,4

d = int(input("Enter the required decimal correctness: "))
tol = 10**(-d)

result=secand(f,a,b,tol)

if result is None:
    print("No solution")
else:
    root,fval,count=np.round(result,d+1)
    print("Iteration: ",count)
    print("Root: ",root, "\nFunctional Value: ",fval)
    xvals=np.linspace(root-10,root+10,101)
    yvals=f(xvals)
    import matplotlib.pyplot as plt
    plt.figure()
    plt.scatter(root,f(root),marker="x",color="Black",label=f"({root:.{d+1}f},0)")  
    plt.plot(xvals,yvals,label="f(x) = xsin(x) + cos(x)")
    plt.axvline(root)
    plt.axhline(0)
    plt.legend(loc="upper left")
    plt.grid()
    plt.title("Secand with visualization")
    plt.show()
    