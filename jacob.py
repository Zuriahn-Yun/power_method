import numpy as np 
import math
from decimal import Decimal, getcontext
getcontext().prec = 3
# 2-norm
def norm(x):
    res = 0
    for i in range(len(x)):
        res += x[i] ** 2
    item = res.item()
    return Decimal(item).sqrt()

def jacobi(A,b):
    k = 1
    x = np.array([0,0,0,0])
    print("Current X")
    print(x)
    x_new = np.array([0,0,0,0])
    while norm(b - np.matmul(A,x)) > 10 ** -6:
        for i in range(4):
            sig = 0
            for j in range(4):
                if j != i:
                    sig = sig + A[i,j] * x[j]
            x_new[i] = (b[i] - sig) / A[i,i]
        x = x_new.copy()
        print("Iteration: ", k)
        k+=1
        print("Current X")
        print(x)
        print("Error:")
        print(norm(b - np.matmul(A,x)))
    return x

def gauss_seidel(A,b):
    k = 1
    x = np.array([0,0,0,0])
    print("Current X")
    print(x)
    while norm(b - np.matmul(A,x)) > 10 ** -6:
        for i in range(4):
            sig = 0
            for j in range(4):
                if j != i:
                    sig += A[i,j] * x[j]
            x[i] = (b[i] - sig) / A[i,i]
        print("Iteration:",k)
        print("X:", x)
        print("Error: ",norm(b - np.matmul(A,x)))
        k+=1
    return x

def sor(A,b,w):
    x = np.array([0,0,0,0])
    k = 1
    while norm(b - np.matmul(A,x)) > 10 ** -6:
        print("Iteration: ", k)
        for i in range(4):
            sig = 0
            for j in range(4):
                if i != j:
                    sig += A[i,j]* x[j]
            x[i] = (1 - w)*x[i] + w*(b[i] - sig)/ A[i,i]
        print("X:", x)
        print("Error: ",norm(b - np.matmul(A,x)))
        k+=1
    return x

if __name__ == "__main__":
    A = np.array([[5,2,1,1],
                  [2,6,2,1],
                  [1,2,7,2],
                  [1,1,2,8]])
    b = np.array([29,31,26,19])
    # Correct answer is [4,3,2,1]
    print("----------------------------")
    print("Jacobis")
    jacobi(A,b)
    print("----------------------------")
    print("Gauss Seidel")
    gauss_seidel(A,b)
    print("----------------------------")
    print("SOR Method")
    sor(A,b,1.1)