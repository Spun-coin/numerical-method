import numpy as np
def gauss_seidel(x1,x2,x3,tol):
    print("Itr\tx1\t\tx2\t\t  x3")
    count=1
    while True:
        x1_new=(17-x2+2*x3)/20
        x2_new=(-18-3*x1_new+x3)/20
        x3_new=(25-2*x1_new+3*x2_new)/20

        print(f"{count}:  {x1_new:.3f},  {x2_new:.3f},  {x3_new:.3f}")

        if(abs(x1_new - x1) < tol and
           abs(x2_new - x2) < tol and
           abs(x3_new - x3) < tol):
            print("\nSolution: ")
            print(f"x1 = {x1_new:.3f},  x2 = {x2_new:.3f},  x3 = {x3_new:.3f}")
            break
        count += 1
        if count > 100:
            raise Exception("There is no solution")
        x1, x2, x3 = x1_new, x2_new, x3_new

x1, x2, x3 = [0.0] * 3
tol = 0.000005
gauss_seidel(x1,x2,x3,tol)