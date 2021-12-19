"""
3.  Write a Python program to draw a line using given axis values
    taken from a text file, with suitable
    label in the x axis, y axis and a title
"""

import matplotlib.pyplot as plt

with open("Pgm3.txt") as f:
    points = f.read()

points = points.split(',')

x = [i.split(' ')[0] for i in points]
y = [i.split(' ')[1] for i in points]
plt.plot(x, y)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph')
plt.show()