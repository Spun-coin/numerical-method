import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,3,5,7,9],dtype=int)
y=np.array([3.142,0.0994,0.0199,0.006,0.003],dtype=float)
xlen=len(x)
ylen=len(y)
n=xlen

if(xlen != ylen or xlen < 2):
    raise Exception ("Data unequal")

sumX=np.sum(np.log(x))
sumY=np.sum(np.log(y))
sumXX=np.sum(np.log(x)*np.log(x))
sumXY=np.sum(np.log(x)*np.log(y))

a=np.exp((sumX*sumXY-sumY*sumXX)/(sumX*sumX-n*sumXX))
b=(sumY-n*np.log(a))/sumX


fx= f"y = {a:0.3f} x^{b:0.3f}"

xmin = np.min(x)
xmax = np.max(x)
ymin = a*np.power(xmin,b)
ymax = a*np.power(xmax,b)

xvals=np.linspace(min(x),max(x),100)
yvals=a*np.power(xvals,b)

plt.figure()
plt.scatter(x,y, color = "red", marker = "x", label = "Actual Data")
plt.plot(xvals, yvals, color = "green", label = fx)
plt.title("Power Curve Fitting")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend(loc="upper right")
plt.show()

