'''NumPy program to create a 4*4 array with random values, now create a new array from the said array swapping first and last rows'''
import numpy as np
ar1 = np.arange(16).reshape(4,4)
print("\n----------------------------------------------------------------")
print("Array \n",ar1)
print("----------------------------------------------------------------\nNew array after swapping first and last rows")
ar1[[0,3]]=ar1[[3,0]]
print("----------------------------------------------------------------\n",ar1)
print("----------------------------------------------------------------\n")
