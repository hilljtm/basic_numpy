import numpy as np
np.random.seed(0) #seed for reproducibility 


x1 = np.random.randint(10, size=6)  # one dimensonal array
x2 = np.random.randint(10, size=(3, 4))  # two dimensonal array
x3 = np.random.randint(10, size=(3, 4, 5)) # three dimensonal array

# ndim = number of dimensions
# shape = size of each dimension
# size = total size of the array
print('x3 ndim: ', x3.ndim) # = 3
print('x3 shape: ', x3.shape) # = 3, 4, 5
print('x3 size: ', x3.size) # = 60

# dtype = data type of array
print('dtype: ', x3.dtype)  # = int64

# item size = lists the size in bytes of each array element, and nbytes
# nbytes = total size in bytes of the array
print('itemsize: ', x3.itemsize, 'bytes') # itemsize = 8 bytes
print('nbytes: ', x3.nbytes, 'bytes')  # nbytes = 480 bytes
# in general, we expect nbytes is equal to itemsize times size





