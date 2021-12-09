'''NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array'''
import numpy as np
a = np.array([[10,12,24],[12,4,8]])
print("\n--------------------------------\nArray\n",a,"\n--------------------------------")
print("Sum of all elements :",np.sum(a),"\n--------------------------------")
print("Sum of each column  :",np.sum(a, axis=0),"\n--------------------------------")
print("Sum of each row     :",np.sum(a, axis=1),"\n--------------------------------")
