'''Write Python program to create two matrices (read values from user) and find the following
3. Trace'''

import numpy as np
def matrix():
  r=c=int(input("Enter The Dimension of Square Matrix(n) : "))
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
print("---------------------------------\nTrace\n---------------------------------\n",np.trace(m1),"\n---------------------------------")