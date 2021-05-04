import numpy as np
import sys

# a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(a[0])

#? array filled with zeroes
# print(np.zeros(2))

#? array filled with ones
# print(np.ones(3))

#? empty array
# print(np.empty(4))

#? array with a range of elements
# print(np.arange(6))

#! (first number,last number,step size)
# b = np.arange(2,9,2)
# print(b)

#* specifying data type default data type is float64
# x = np.ones(2, dtype=np.int64)

#? 2d array
# z = np.zeros((3,4))
# print(z)

#? reshaping an array
# np.set_printoptions(threshold=sys.maxsize) [this statement is use to print full size of the array] 
# print(np.arange(10000).reshape(100,100))

#! Basic Operators
a = np.array([20,30,40,50])
b = np.arange(4)
c = a - b
print(c)

# squaring every elements
d = b**2 
print(d)
# sin of every elements
print(np.sin(a))
# checks all the elements
print(a<35)