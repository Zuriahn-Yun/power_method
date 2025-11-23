import numpy as np
import math

# i is number of iterations
# A is starting Matrix
def power(A,iterations):
    x = np.array([1,1])
    for i in range(iterations):
        print("Iteration Number:", i)
        curr = np.matmul(A,x)
        print("A Times previous X")
        print(curr)
        x = curr  * 1/norm(curr)
        print("X Normalized, Iteration:", i)
        print(x)
    return x

# 2-norm
def norm(x):
    res = 0
    for i in range(len(x)):
        res += x[i] ** 2
    return math.sqrt(res)

if __name__ == "__main__":
    A = np.array([[2,-12],
                 [1,-5]])
    power(A,6)