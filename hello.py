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
# a = np.array([20,30,40,50])
# b = np.arange(4)
# c = a - b
# print(c)

# squaring every elements
# d = b**2 
# print(d)
# sin of every elements
# print(np.sin(a))
# checks all the elements
# print(a<35)

# A = np.array( [[1,1],
#                [0,1]] )

# B = np.array([[2,0],
#               [3,4]] )

# elementwise product
# print(A*B)
# matrix product
# print(A@B)
# another matrix product method
# print(A.dot(B))

# sorting
arr = np.array([2,1,5,3,7,4,6,8])
print(np.sort(arr))

# concatenate
a = np.array([1,3,4,2])
b = np.array([5,7,8,6])
print(np.concatenate((a,b)))

# 2d concatenate
x = np.array([[1,2],[3,4]])
y = np.array([[5,6]])
print(np.concatenate((x,y), axis = 0))


arr_eg = np.array([[[0,1,2,3],
                    [4,5,6,7]],
                    
                    [[0,1,2,3],
                     [4,5,6,7]],
                     
                    [[0,1,2,3],
                     [4,5,6,7]]])
# number of dimensions
print(arr_eg.ndim)
# size
print(arr_eg.size)

# another way of reshaping
arr1 = np.arange(6)
# order: C means to read/write the elements using C-like index order, F means to read/write the elements using Fortran-like index order, A means to read/write the elements in Fortran-like index order if a is Fortran contiguous in memory, C-like order otherwise. (This is an optional parameter and doesn’t need to be specified.)
print(np.reshape(arr1, newshape=(1,6), order ='C'))

# how to add a new axis
arr2 = np.array([1,2,3,4,5,6])
print(arr2.shape)
arr3 = arr2[np.newaxis, :]
print(arr3.shape)

# converting in row vector and column vector
row_vec = arr2[np.newaxis, :]
print(row_vec.shape)
col_vec = arr2[:,np.newaxis]
print(col_vec.shape)

# changing index position to 1 
b0 = np.expand_dims(arr2, axis=1)
print(b0.shape)
c0 = np.expand_dims(arr2, axis=0)
print(c0.shape)

# indexing and slicing 
data = np.array([1,2,3])
print(data[1])
print(data[0:2])
print(data[1:])
print(data[-2:])
print(data[-3:])

d = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# unsorted result
print(a[a<5])
# sorted result
print(np.sort(d[d<5]))

five_up = (d >= 5)
print(d[five_up])

div_by_2 = d[d%2==0]
print(div_by_2)

c = d[(d > 2) & (a < 11)]
print(c)

fiveup = (d>5)|(d==5)
print(fiveup)

arrr=np.nonzero(d<5)
print(arrr)

list_of_coordinates = list(zip(arrr[0],arrr[1]))
for coord in list_of_coordinates :
    print(coord)

print(d[arrr])

# empty nonzero 
not_there = np.nonzero(d == 42)
print(not_there)

a1 = np.array([1,2,3,4,5,6,7,8,9,10])
arr0 = a1[3:8]
print(arr0)

a2 = np.array([[1,1],
               [2,2]])

a3 = np.array([[3,3],
               [4,4]])

print(np.vstack((a2,a3)))
print(np.hstack((a2,a3)))

x = np.arange(1,25).reshape(2,12)
print(x)
print(np.hsplit(x,3))
print(np.hsplit(x,(3,4)))

# copying syntax: b = a.copy()

datas = np.array([1,2])
ones = np.ones(2, dtype=int)
print(datas + ones)
print(datas - ones)
print(datas * ones)
print(datas / ones)

r = np.array([1,2,3,4])
print(r.sum())

p = np.array([[1,1],[2,2]])
# row-wise sum
print(p.sum(axis=0))
# column-wise sum
print(p.sum(axis=1))

# broadcasting(vector and scalar opertions)
d1 = np.array([1.0,2.0])
print(d1*1.6)

a4 = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
               [0.54627315, 0.05093587, 0.40067661, 0.55645993],
               [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

print(a4.sum())
print(a4.min())
print(a4.max())
print(a4.min(axis=0)) # axis = 0 denotes column
print(a4.min(axis=1)) # axis = 1 denotes row