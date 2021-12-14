''' Write Python program to create two matrices (read values from user) and find the following
5. Determinant '''

import numpy as np
def matrix():
  r=int(input("Enter Number of Rows    : "))
  c=int(input("Enter Number of Columns : "))
  l=[]
  while(len(l)!=r*c):
    print("Enter ",r*c, " Elements Separated By Space ")
    l = list(map(int,input().split()))
    if(len(l)!=r*c):
      print("Matrix Size Doesn't Match With the Number of Elements Entered.")
  a = np.array(l).reshape(r,c)
  return(a)
m1 = matrix()
print("---------------------------------\nMatrix\n---------------------------------\n",m1)
print("---------------------------------\nDeterminant\n---------------------------------\n",np.linalg.det(m1),"\n---------------------------------")