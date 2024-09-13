import numpy as np


a = np.random.randn(1, 3)
print(a.shape)
b = np.random.randn(3, 3)
print(b.shape)
c = a + b
# print(c)
print(f"{c.shape=}")

x = np.array([[2,1], [1, 3]])



print(np.dot(x, x))

[2,1] dot [2,1]
[1,3]     [1,3] 
=
[[ 5  5]
 [ 5 10]]

 a * (b + c) - (b + c)

# a = np.random.randn(3, 3)
# print(a.shape)
# b = np.random.randn(2, 1)
# print(b.shape)
# c = a + b
# print(f"{c.shape=}")