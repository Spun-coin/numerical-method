import numpy as np
import matplotlib.pyplot as plt
def f(x,y,z):
    return x+z

def g(x,y,z):
    return x-y*y


def Euler(f,g,x0,y0,z0,xn,n):
    h=(xn-x0)/n
    x=np.linspace(x0,xn,n+1)
    y=np.zeros(n+1,dtype="float")
    z=np.zeros(n+1,dtype="float")
    y[0]=y0
    z[0]=z0
    for i in range(n):
        y[i+1]=y[i]+h*f(x[i],y[i],z[i])
        z[i+1]=z[i]+h*g(x[i],y[i],z[i])
    return x,y,z

def RK2(f,g,x0,y0,z0,xn,n):
    h=(xn-x0)/n
    x=np.linspace(x0,xn,n+1)
    y=np.zeros(n+1,dtype="float")
    z=np.zeros(n+1,dtype="float")
    y[0]=y0
    z[0]=z0
    for i in range(n):
        k1=h*f(x[i],y[i],z[i])
        l1=h*g(x[i],y[i],z[i])
        k2=h*f(x[i]+h,y[i]+k1,z[i]+l1)
        l2=h*g(x[i]+h,y[i]+k1,z[i]+l1)
        k=(k1+k2)/2
        l=(l1+l2)/2
        y[i+1]=y[i]+k
        z[i+1]=z[i]+l
    return x,y,z

def RK4(f,g,x0,y0,z0,xn,n):
    h=(xn-x0)/n
    x=np.linspace(x0,xn,n+1)
    y=np.zeros(n+1,dtype="float")
    z=np.zeros(n+1,dtype="float")
    y[0]=y0
    z[0]=z0
    for i in range(n):
        k1=h*f(x[i],y[i],z[i])
        l1=h*g(x[i],y[i],z[i])
        k2=h*f(x[i]+h/2,y[i]+k1/2,z[i]+l1/2)
        l2=h*g(x[i]+h/2,y[i]+k1/2,z[i]+l1/2)
        k3=h*f(x[i]+h/2,y[i]+k2/2,z[i]+l2/2)
        l3=h*g(x[i]+h/2,y[i]+k2/2,z[i]+l2/2)
        k4=h*f(x[i]+h,y[i]+k3,z[i]+l3)
        l4=h*g(x[i]+h,y[i]+k3,z[i]+l3)
        k=(k1+2*k2+2*k3+k4)/6
        l=(l1+2*l2+2*l3+l4)/6
        y[i+1]=y[i]+k
        z[i+1]=z[i]+l
    return x,y,z

x0=0
y0=2
z0=1
xn=1
n=int(input("Enter n for Euler: "))
x_Euler,y_Euler,z_Euler=Euler(f,g,x0,y0,z0,xn,n)
n=int(input("Enter n for RK2: "))
x_RK2,y_RK2,z_RK2=RK2(f,g,x0,y0,z0,xn,n)
n=int(input("Enter n for RK4: "))
x_RK4,y_RK4,z_RK4=RK4(f,g,x0,y0,z0,xn,n)
print(f"The solution at x = {xn} using different methods are:")
print(f"{'Euler':<15}: {y_Euler[-1]:.3f}  {z_Euler[-1]:.3f}")
print(f"{'RK2':<15}: {y_RK2[-1]:.3f}  {z_RK2[-1]:.3f}")
print(f"{'RK4':<15}: {y_RK4[-1]:.3f}  {z_RK4[-1]:.3f}")


plt.figure()
plt.scatter(x_Euler,y_Euler,label="Euler mesh points",marker="o")
plt.plot(x_Euler,y_Euler,color="green",label="Euler method")
plt.scatter(x_RK2,y_RK2,label="RK2 mesh points",marker="x")
plt.plot(x_RK2,y_RK2,color="blue",label="RK2 method")
plt.scatter(x_RK4,y_RK4,label="RK4 mesh points",marker="*")
plt.plot(x_RK4,y_RK4,color="yellow",label="RK4 method")
plt.grid()
plt.title("Solution of ODE")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(loc="upper left")
plt.show()

plt.figure()
plt.scatter(x_Euler,z_Euler,label="Euler mesh points",marker="o")
plt.plot(x_Euler,z_Euler,color="green",label="Euler method")
plt.scatter(x_RK2,z_RK2,label="RK2 mesh points",marker="x")
plt.plot(x_RK2,z_RK2,color="blue",label="RK2 method")
plt.scatter(x_RK4,z_RK4,label="RK4 mesh points",marker="*")
plt.plot(x_RK4,z_RK4,color="yellow",label="RK4 method")
plt.grid()
plt.title("Solution of ODE")
plt.xlabel("x-axis")
plt.ylabel("z-axis")
plt.legend(loc="upper right")
plt.show()
