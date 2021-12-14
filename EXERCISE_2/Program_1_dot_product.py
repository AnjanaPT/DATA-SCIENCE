'''Write Python program to create two matrices (read values from user) and find the following
1. Dot Product'''

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
m2 = matrix()
if(np.shape(m1)[1] == np.shape(m2)[0]):
  print("---------------------------------\nMatrix 1\n---------------------------------\n",m1)
  print("---------------------------------\nMatrix 2\n---------------------------------\n",m2)
  print("---------------------------------\nDot product\n---------------------------------\n",np.dot(m1,m2),"\n---------------------------------")
else:
  print("\nDimensions Doesn't Matching !!!\n(Number of Columns of Matrix 1 Should be Same as Number of Rows of Matrix 2)")