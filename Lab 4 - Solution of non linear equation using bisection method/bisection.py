def f(x):
    return (x*x - 4*x - 10)

#initial guesses
a=5
b=6
temp=0
step=1

while True:
    c = (a+b)/2
    if (f(a)>0*f(b)>0):
        raise Exception("Not good guess")
    
    elif(f(c)<0):
            a=c
            if(f(temp)==f(c)):
                break
            temp=a
    else:
            b=c
            if(f(temp)==f(c)):
                break
            temp=b
    
print(f"{c:.4f}")