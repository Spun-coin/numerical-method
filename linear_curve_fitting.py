import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,3,5,7,9],dtype=int)
y=np.array([2.4569,0.4569,-1.5430,-3.5430,-5.5430],dtype=float)
xlen=len(x)
ylen=len(y)
n=xlen

if(xlen != ylen or xlen < 2):
    raise Exception ("Data unequal")

sumx=np.sum(x)
sumy=np.sum(y)
sumxx=np.sum(x*x)
sumxy=np.sum(x*y)

b=((n*sumxy)-sumy*sumx)/((n*sumxx)-sumx*sumx)
a= ((sumy)-b*sumx)/n

if b < 0:
    sign = "-"
else:
    sign = "+"

fx= f"y = {a:0.3f} {sign} {abs(b):0.3f}x"

xmin = np.min(x)
xmax = np.max(x)
ymin = a+b*xmin
ymax = a+b*xmax

plt.figure()
plt.scatter(x,y, color = "red", marker = "x", label = "Actual Data")
plt.plot([xmin,xmax],[ymin,ymax], color = "green", label = fx)
plt.title("Linear Curve Fitting")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend(loc="upper right")
plt.show()

