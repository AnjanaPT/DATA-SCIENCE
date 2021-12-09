'''NumPy program to multiply two given array of same size element by element'''
import numpy as np
ar1 = np.array([[2,3,5],[1,2,3],[5,2,1]])
ar2 = np.array([[1,3,2],[4,2,5],[6,3,1]])
print("\n--------------------------------\nArray 1\n--------------------------------")
print(ar1)
print("--------------------------------\nArray 2\n--------------------------------")
print(ar2)
print("--------------------------------\nMultiplication(Element wise)\n--------------------------------")
print(np.multiply(ar1,ar2),"\n--------------------------------\n")