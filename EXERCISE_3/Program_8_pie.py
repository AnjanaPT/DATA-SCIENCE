"""
8. Write a Python programming to create a pie chart
   of the popularity of programming Languages.

Programming languages: Java  Python  PHP  JavaScript  C#  C++
Popularity           : 22.2  17.6    8.8  8           7.7 6.7
"""

import matplotlib.pyplot as plt
import numpy as np

pop = np.array([22.2, 17.6, 8.8, 8, 7.7, 6.7])
course = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
color = ['r', 'gray', 'teal', 'lime', '#800040', 'y']
plt.figure(figsize=(8, 6))
plt.pie(pop, labels=course, colors=color, autopct='%1.1f%%')
plt.show()
