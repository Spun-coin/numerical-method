import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,3,5,7,9],dtype=int)
y=np.array([0.342,0.090,0.023,0.006,0.001],dtype=float)
xlen=len(x)
ylen=len(y)
n=xlen

if(xlen != ylen or xlen < 2):
    raise Exception ("Data unequal")

sumx=np.sum(x)
sumY=np.sum(np.log(y))
sumxx=np.sum(x*x)
sumxY=np.sum(x*np.log(y))

b=(n*sumxY-sumY*sumx)/(n*sumxx-sumx*sumx)
a= np.exp((sumY-b*sumx)/n)


fx= f"y = {a:0.3f} e^{b:0.3f}x"

xmin = np.min(x)
xmax = np.max(x)
ymin = a*np.exp(b*xmin)
ymax = a*np.exp(b*xmax)

xvals=np.linspace(min(x),max(x),100)
yvals=a*np.exp(b*xvals)

plt.figure()
plt.scatter(x,y, color = "red", marker = "x", label = "Actual Data")
plt.plot(xvals, yvals, color = "green", label = fx)
plt.title("Exponential Curve Fitting")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend(loc="upper right")
plt.show()

