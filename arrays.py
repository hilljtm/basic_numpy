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

# Array Indexing: accessing single elements
x1  # = array([5, 0, 3, 3, 7, 9])
x1[0]  # = 5
x1[4]  # = 7

# indexing from the end of the array
x1[-1]  # = 9
x1[-2] # = 7

# multi dimensional array by using comma seperated tuple of indices 
x2  # = array([[3, 5, 2, 4]])
            #  [7, 6, 8, 8]
            #  [1, 6, 7, 7]])

x2[0, 0]  # = 3
x2[2, 0]  # = 1
x2[2, -1]  # = 7

# modifying values using any of above index notation
x2[0, 0] = 12
x2  # = array([[12, 5, 2, 4],
            #  [7, 6, 8, 8],
            #  [1, 6, 7, 7]])

#NOTE: unlike python lists, numpy arrays have a fixed type
# attempt to insert a floating-point value to an integer array, the value will be silently truncated
x1[0] = 3.14159  # this will be truncated
x1  # = array([5, 0, 3, 3, 7, 9])

# Array slicing: accessing subarrays 
#NOTE: slicing syntax,if any are unspecified, the default values are start=0, stop=size of dimension, step=1
# x[start:stop:step]

# One dimensional subarrays
x = np.arange(10)
x  # = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# first five elements
x[:5]  # = array([0, 1, 2, 3, 4])

# elements after index 5
x[5:]  # = array([5, 6, 7, 8, 9])

# middle subarray
x[4:7]  # = array([4, 5, 6])

# every other element
x[::2]  # = array([0, 2, 4, 6, 8])

# every other element, starting at index 1
x[1::2]  # = array([1, 3, 5, 7, 9])

#NOTE: negative step value defaults for start and stop to be swapped, allowing a way to reverse an array
# all elements reversed
x[::-1]  # = array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

# reversed every other from index 5
x[5::-2]  # = array([5, 3, 1])



