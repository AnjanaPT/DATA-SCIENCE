"""
4 Write a Python program to plot two or more lines on same plot
  with suitable legends of each line
"""

import matplotlib.pyplot as plt


x1 = [10,30]
y1 = [10,30]
plt.plot(x1, y1, label = "Line 1")

x2 = [30,50]
y2 = [50,30]
plt.plot(x2, y2, label = "Line 2")

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.title('Two Lines plot')

plt.legend()
plt.show()