# Importing the NumPy library with an alias 'np'
import numpy as np

# Creating a NumPy array 'a' containing elements 1, 0, NaN (Not a Number), and infinity
a = np.array([1, 0, np.nan, np.inf])

# Printing the original array 'a'
print("Original array")
print(a)

# Checking the given array 'a' element-wise for finiteness and printing the result

print(np.isfinite(a))