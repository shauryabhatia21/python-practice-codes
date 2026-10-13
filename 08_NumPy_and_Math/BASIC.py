# Numpy = Numerical Python
import numpy as np

# NumPy PROVIDES:
# 1. Fast multi-dimensional arrays (ndarray)
# 2. Mathematical functions
# 3. Linear algebra tools
# 4. Random number generations
# 5. Broadcasting (vectorized computation)

# Why NumPy is Faster Than List?
# Lists:
#  1. Store mixed types
#  2. Not memory efficient
#  3. No vectorization

# ----- ARRAY PROPERTIES -----
arr8 = np.array([[1,2,3],[4,5,6]])

# 1. Tell the dimensions:
print(arr8.ndim)

# 2. Tell the shape:
print(arr8.shape)

# 3. Tell the size (count all elements):
print(arr8.size)

# 4. Tell the type:
print(arr8.dtype)

# ----- CREATING ARRAY -----
arr1 = np.array([1,2,3])
print(arr1)

# CREATING 2D ARRAY:
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

# CONVERT TO ZEROS ARRAY:
arr3 = np.zeros((2,3))
print(arr3)

# CREATING ALL THE ELEMENTS AS 1:
arr4 = np.ones((2,2))
print(arr4)

# CREATING IDENTITY MATRIX:
arr5 = np.eye(3)
print(arr5)

# ARANGE FUNCTION IN 1D ARRAY:
# first value = starting
# second value = ending
# third value = step
arr6 = np.arange(0,10,2)
print(arr6)

# CREATING EVENLY SPACED VALUES:
arr7 = np.linspace(0,1,5)
# Use For:
#  * You need equal spacing
#  * Plotting graphs
print(arr7)

# ----- INDEXING AND SLICING -----
# Indexing and slicing is same as in case of list
# Note:
#   * Slicing creates a view, not a copy

# Example (view):
a1 = np.array([11,22,33,44,55])
a2 = a1[::]
a2[1] = 99
print("After view modification:", a1)

# Making a copy:
a1 = np.array([11,22,33,44,55])
a2 = a1.copy()
a2[1] = 99
print("After copy modification:", a1)

# ----- MATHEMATICAL OPERATIONS -----
a = np.array([1,2,30])
b = np.array([4,5,6])

# Adding:
print("Add:", a + b)

# Multiplication:
print("Multiply:", a * b)

# Square root:
print("Sqrt:", np.sqrt(a))

# Exponents:
print("Exp:", np.exp(a))

# Log:
print("Log:", np.log(a))

# ----- AGGREGATION FUNCTIONS -----
arr = np.array([10,20,30,40])

# Sum:
print("Sum:", np.sum(arr))

# Mean:
print("Mean:", np.mean(arr))

# Standard deviation:
print("Std:", np.std(arr))

# Reshaping array:
arr_reshape = np.arange(1,13)

# Reshape:
print("Reshaped:\n", arr_reshape.reshape(3,4))

# Automatic dimension:
print("Auto reshape:\n", arr_reshape.reshape(3,-1))

# ----- BOOLEAN MASKING -----
arr9 = np.array([10,20,30,40])
mask = arr9 > 25
print("Mask:", mask)
print("Filtered:", arr9[mask])

# ----- MATRIX MULTIPLYING -----
mat_a = np.array([[1,2],[3,4]])
mat_b = np.array([[5,6],[7,8]])
print("Matrix multiply:\n", mat_a @ mat_b)

# ----- RANDOM NUMBER -----
print("Random integers:", np.random.randint(1,10,5))
