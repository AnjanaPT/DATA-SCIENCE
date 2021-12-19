"""
5. Write a Python program to create multiple plots.
"""

import matplotlib.pyplot as plt

figure, axis = plt.subplots(1,2)


x1 = [10,30]
y1 = [10,30]
axis[0].plot(x1, y1)
axis[0].set_title("Plot 1")

x2 = [30,50]
y2 = [50,30]
axis[1].plot(x2, y2)
axis[1].set_title("Plot 2")

plt.show()
