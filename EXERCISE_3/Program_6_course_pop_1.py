"""
6. Consider the following data.
Programming languages: Java  Python  PHP  JavaScript  C#  C++
Popularity             22.2  17.6    8.8  8           77  6.7
(i) Write a Python programming to display a bar chart
    of the popularity of programming Languages.
"""

import numpy as np
import matplotlib.pyplot as plt


# Creating the dataset
c_pop = {'Java':22.2, 'Python':17.6, 'PHP':8.8,'JavaScript':8,'C#':77,'C++':6.7}

courses = list(c_pop.keys())
popularity = list(c_pop.values())

plt.figure(figsize = (8,5))

# Plot Bar Chart
plt.bar(courses, popularity, color ='teal',width = 0.5)

plt.xlabel("Programming Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Languages")
plt.show()


