''''NumPy program to create an element-wise comparison of two given arrays''''
import numpy as np
ar1 = np.array([[10,20,8],[-5,15,-7]])
ar2 = np.array([[10,-10,8],[-5,22,44]])
print("\n--------------------------------\nArray 1\n--------------------------------\n")
print(ar1)
print("\n--------------------------------\nArray 2\n--------------------------------\n")
print(ar2)
print("\n--------------------------------\nComparison")
print("\n--------------------------------\nIf Array1 > Array2(Element wise)\n--------------------------------\n")
print(np.greater(ar1,ar2))
print("\n--------------------------------\nIf Array1 >= Array2(Element wise)\n--------------------------------\n")
print(np.greater_equal(ar1,ar2))
print("\n--------------------------------\nIf Array1 < Array2(Element wise)\n--------------------------------\n")
print(np.less(ar1,ar2))
print("\n--------------------------------\nIf Array1 <= Array2(Element wise)\n--------------------------------\n")
print(np.less_equal(ar1,ar2),"\n--------------------------------\n")