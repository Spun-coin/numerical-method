x=[0,1,2,3,4] #x-values
y=[-9,-8,11,66,175] #y-values
n=len(x)
table=[[0.0 for i in range(n)]for j in range(n)]

for i in range(n):
    table[i][0]=y[i]

for j in range(1,n):
    for i in range(j,n):
        table[i][j]=table[i][j-1]-table[i-1][j-1]

print("Backward difference table:")
for i in range(n):
    for j in range(i+1):
        print(f"{table[i][j]}",end=" ")
    print("\n")

xval=3.6 #put x value to interpolate
p=((xval-x[4])/(x[1]-x[0]))
a=table[4][0]
b=p*table[4][1]
c=(p*(p+1))*table[4][2]/2
d=(p*(p+1)*(p+2))*table[4][3]/6
e=(p*(p+1)*(p+2)*(p+3))*table[4][4]/24


yval=a+b+c+d+e
print(yval)