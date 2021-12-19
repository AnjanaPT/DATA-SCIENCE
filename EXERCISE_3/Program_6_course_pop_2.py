"""
6. Consider the following data.
Programming languages: Java  Python  PHP  JavaScript  C#  C++
Popularity             22.2  17.6    8.8  8           77  6.7
(ii) Write a Python programming to display a horizontal bar chart
of the popularity of programming
Languages(Give Red colour to the bar chart).
"""

import numpy as np
import matplotlib.pyplot as plt


# Creating the dataset
c_pop = {'Java':22.2, 'Python':17.6, 'PHP':8.8,'JavaScript':8,'C#':77,'C++':6.7}

courses = list(c_pop.keys())
popularity = list(c_pop.values())

plt.figure(figsize = (8,6))

# Plot Bar Chart
plt.barh(courses, popularity, color ='red',height=0.8)

plt.xlabel("Popularity")
plt.ylabel("Programming Languages")
plt.title("Popularity of Programming Languages")
plt.show()
