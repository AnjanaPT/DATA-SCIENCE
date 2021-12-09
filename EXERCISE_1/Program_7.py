'''NumPy program to save a given array to a text file and load it'''
import numpy as np
import os
a = np.arange(20,40).reshape(5, 4)
print("\n----------------------------------------------------------------\nArray\n",a)
np.savetxt('temp.txt', a, fmt="%d", header='matrix')
print("----------------------------------------------------------------\nAfter loading, content of the text file\n",np.loadtxt('temp.txt'))
print("----------------------------------------------------------------")
