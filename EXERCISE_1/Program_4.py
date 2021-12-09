'''NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15'''
import numpy as np
a = np.arange(21)
print("\n--------------------------------------------------------------------------")
print("Vector : ",a,"\n--------------------------------------------------------------------------\n")
print("\nChange the sign of numbers in the range from 9 to 15")
a[(a >= 9) & (a <= 15)] *= -1
print(a,"\n--------------------------------------------------------------------------\n")
