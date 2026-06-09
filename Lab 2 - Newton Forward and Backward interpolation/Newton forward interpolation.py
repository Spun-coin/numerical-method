x=[0,1,2,3,4] #x-values
y=[-9,-8,11,66,175] #y-values
n=len(x)
table=[[0.0 for i in range(n)]for j in range (n)]

for i in range (n):
    table[i][0]=y[i]

for j in range (1,n):
    for i in range (0,n-j):
        table[i][j]=table[i+1][j-1]-table[i][j-1]

print("Forward difference table:")
for i in range(n):
    for j in range(0,n-i):
        print(f"{table[i][j]}",end="\t")
    print("\n")

xval=0.7 #put x-value to interpolate
p = (xval-x[0])/(x[1]-x[0])
a=table[0][0]
b=p*(table[1][0]-table[0][0])
c=((p*(p-1)/2))*(table[1][1]-table[0][1])
d=((p*(p-1)*(p-2))/6)*(table[1][2]-table[0][2])
e=((p*(p-1)*(p-2)*(p-3)/24)*(table[1][3]-table[0][3]))


yval=a+b+c+d+e
print(f"y({xval}) = {yval}")