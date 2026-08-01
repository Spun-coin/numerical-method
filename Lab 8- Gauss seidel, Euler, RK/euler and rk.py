import numpy as np
import matplotlib.pyplot as plt
def f(x,y):
    return x+y

def real(x): #solution of the differential equation solved using math 
    return 2*np.exp(x)-x-1

def Euler(f,x0,y0,xn,n):
    h=(xn-x0)/n
    x=np.linspace(x0,xn,n+1)
    y=np.zeros(n+1,dtype="float")
    y[0]=y0
    for i in range(n):
        y[i+1]=y[i]+h*f(x[i],y[i])
    return x,y

def RK2(f,x0,y0,xn,n):
    h=(xn-x0)/n
    x=np.linspace(x0,xn,n+1)
    y=np.zeros(n+1,dtype="float")
    y[0]=y0
    for i in range(n):
        k1=h*f(x[i],y[i])
        k2=h*f(x[i]+h,y[i]+k1)
        k=(k1+k2)/2
        y[i+1]=y[i]+k
    return x,y

def RK4(f,x0,y0,xn,n):
    h=(xn-x0)/n
    x=np.linspace(x0,xn,n+1)
    y=np.zeros(n+1,dtype="float")
    y[0]=y0
    for i in range(n):
        k1=h*f(x[i],y[i])
        k2=h*f(x[i]+h/2,y[i]+k1/2)
        k3=h*f(x[i]+h/2,y[i]+k2/2)
        k4=h*f(x[i]+h,y[i]+k3)
        k=(k1+2*k2+2*k3+k4)/6
        y[i+1]=y[i]+k
    return x,y

x0=0
y0=1
xn=1
n=int(input("Enter n for Euler: "))
x_Euler,y_Euler=Euler(f,x0,y0,xn,n)
n=int(input("Enter n for RK2: "))
x_RK2,y_RK2=RK2(f,x0,y0,xn,n)
n=int(input("Enter n for RK4: "))
x_RK4,y_RK4=RK4(f,x0,y0,xn,n)
n=int(input("Enter n for real: "))
x_real=np.linspace(x0,xn,n+1)
y_real=real(x_real)
print(f"The solution at x = {xn} using different methods are:")
print(f"{'Exact solution':<15}: {y_real[-1]:.3f}")
print(f"{'Euler':<15}: {y_Euler[-1]:.3f}")
print(f"{'RK2':<15}: {y_RK2[-1]:.3f}")
print(f"{'RK4':<15}: {y_RK4[-1]:.3f}")
plt.figure()
plt.scatter(x_Euler,y_Euler,label="Euler mesh points",marker="o")
plt.plot(x_Euler,y_Euler,color="green",label="Euler method")
plt.scatter(x_RK2,y_RK2,label="RK2 mesh points",marker="x")
plt.plot(x_RK2,y_RK2,color="blue",label="RK2 method")
plt.scatter(x_RK4,y_RK4,label="RK4 mesh points",marker="*")
plt.plot(x_RK4,y_RK4,color="yellow",label="RK4 method")
plt.scatter(x_real,y_real,label="Exact solution mesh points",marker="+")
plt.plot(x_real,y_real,color="red",label="Exact solution")
plt.grid()
plt.title("Solution of ODE")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(loc="upper left")
plt.show()
