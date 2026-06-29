import numpy as np
import matplotlib.pyplot as plt

x = [1,3,4,7,10]
y = [97,42,59,61,10]
xlen=len(x)
ylen=len(y)
n=xlen

if(xlen != ylen or xlen<2):
    raise Exception("Data unequal or less than 2")

xp = 5

def lagrange(x,y,xp):
    yp=0
    for i in range (n):
        mul=1
        for j in range(n):
            if(i!=j):
                mul*=((xp-x[j])/(x[i]-x[j]))
        yp+=y[i]*mul
    return yp

yp=lagrange(x,y,xp)
xnew=np.linspace(1,10,101)
ynew=lagrange(x,y,xnew)

print(f"y({xp}) = {yp}")

plt.figure()
plt.scatter(x,y,color="GREEN",label="dataset")
plt.scatter(xp,yp,color="red",label="Interpoled",marker="x")
plt.plot(xnew,ynew,color="BLACK",label="function")
plt.title("Lagrange Interpolation")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(loc="upper left")
plt.grid()
plt.show()
