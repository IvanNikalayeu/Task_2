import numpy as np

# arr = np.full(10, 2.5)
# print(arr)
#

# arr = np.zeros(10)
# arr[5] = 1
# print(arr)

# arr = np.arange(10,50)
# print(arr)

# arr = np.arange(10)
# arr_1 = arr[: : -1]
# print(arr_1)
#
# arr = np.arange(9).reshape(3,3)
# print(arr)
#

# arr = np.array([1,2,0,0,4,0])
# print(arr)
# print(arr[(arr != 0)])
# arrr = np.nonzero(arr)
# print(arrr)

# arr = np.ones(9).reshape(3,3)
# print(arr)
# arr_1 = np.eye(3)
# print(arr_1)

# arr = np.random.random((3,3,3))
# print(arr)

# arr = np.random.random((10,10))
# print(arr)
# print(arr.min())
# print(arr.max())

# arr = np.random.random(30)
# print(arr.mean())

# arr = np.zeros((10,10))
#
# arr[0:1] = 1
# arr[:, 0:1] = 1
# arr[-1] = 1
# arr[:, -1] = 1
# print(arr)

# print(0 * np.nan)
# print(np.nan == np.nan)
# print(np.inf > np.nan)
# print(np.nan - np.nan)
# print(3 == 3 * 0.1)

# arr = np.diag(np.arange(1,5), k=-1)
# print(arr)

arr = np.zeros((8,8), dtype=int)
arr[1: :2, ::2] = 1
arr[::2, 1::2] = 1
print(arr)







