#Consider the system of LINEAR equations
#x + y + z = 6
#2y + 5z  = -4
#2x + 5y - z = 27

#This is the same as 
#|1 1  1| |x| = | 6|
#|0 2  5| |y| = |-4|
#|2 5 -1| |z| = |27|
#  A       X     B

# A*X = B
# X = B/A = B*A^-1

import numpy as np

A = np.array([[1,1,1],[0,2,5],[2,5,-1]])
B = np.array([[6],[-4],[27]])
B_test = np.array([6,-4,27])

X = np.dot(np.linalg.inv(A),B)
print(f'x is {X[0]}, y is {X[1]} and z is {X[2]}')

XX = np.linalg.solve(A,B)
print(XX)


#cross product example

a = np.array([[1],[0],[0]])
b = np.array([[0],[1],[0]])
cross = np.cross(b,a,axis=0)

#laplace transform exampnle

import sympy as sp
s, t = sp.symbols('s t')
trans_func = 1/((s+0.2+0.5j)*(s+0.2-0.5j))
result = sp.inverse_laplace_transform(trans_func, s, t)









