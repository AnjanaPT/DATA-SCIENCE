"""
7. Write a Python program to create bar plot of
scores by group and gender. Use multiple X values on
the same chart for men and women.
Sample Data:
Means (men) = (22, 30, 35, 35, 26)
Means (women) = (25, 32, 30, 35, 29)
"""

import numpy as np
import matplotlib.pyplot as plt

y1 = [22,30,35,35,26]
y2 = [25,32,30,35,29]
x_labels = ['G1','G2','G3','G4','G5']
x1 = np.arange(5)
width = 0.4
plt.figure(figsize = (9, 6))

plt.bar(x1-0.2,y1,color="black",width=width,label='Men')
plt.bar(x1+0.2,y2,color="teal",width=width,label='Women')
plt.xticks(x1,x_labels)



plt.xlabel("Person")
plt.ylabel("Scores")
plt.legend()

plt.title("Scores by Group and Gender")
plt.show()
