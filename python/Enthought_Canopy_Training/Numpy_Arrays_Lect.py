import numpy as np 

# Simple Array Creation
lst = [0, 1, 2, 3]
a = np.array(lst)

print lst # [0, 1, 2, 3]
print a #[0 1 2 3]

# Checking the type
print type(a) # <type 'numpy.ndarray'>, upper limit of number of dimensions (nd) = 32

# Numeric 'Type' of Elements
print a.dtype # int64

# Bytes per elements
print a.itemsize # 8

# Array Shape
# - Shape returns a tuple listing the length of the array along each dimension
print a.shape 		# (4,)
print np.shape(a)	# (4,)

# Array Size
# - Size repots the entire number of elements in an array
print a.size 		# 4
print np.size(a)	# 4

# Bytes of Memory Used
# Return the number of bytes used by the data portion of the array
print a.nbytes 		# 32

# Number of Dimensions
print a.ndim		# 1

# Array Indexing & Slicing
# Array Indexing
print a[0]			# 0
a[0] = 10
print a 			# [10  1  2  3]

# Fill
# Set all values in an array
a.fill(0)
print a 			# [0 0 0 0]

# This also works, but may be slower.
a[:] = 1
print a 			# [1 1 1 1]

# Beware of type coercion
print a.dtype  		# int64

# Assigning a float into an int32 array truncates the decimal part
a[0] = 10.6
print a 			# [10  1  1  1]

# Fill has the same behavior
a.fill(-4.8)
print a 			# [-4 -4 -4 -4]

# Slicing
#
# var[lower:upper:step]
#
# Slicing arrays
# indices: 0 1 2 3 4
a = np.array([10, 11, 12, 13, 14])
print a  			# [10 11 12 13 14]








