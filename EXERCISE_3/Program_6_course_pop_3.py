"""
6. Consider the following data.
Programming languages: Java  Python  PHP  JavaScript  C#  C++
Popularity             22.2  17.6    8.8  8           77  6.7
(iii) Write a Python programming to display a bar chart of the
      popularity of programming Languages.
      Use different color for each bar.
"""


import numpy as np
import matplotlib.pyplot as plt


# Creating the dataset
c_pop = {'Java':22.2, 'Python':17.6, 'PHP':8.8,'JavaScript':8,'C#':77,'C++':6.7}
c_pop_color=['black','gray','teal','lime','#800040','#bf80ff']

courses = list(c_pop.keys())
popularity = list(c_pop.values())

plt.figure(figsize = (10, 5))

# Plot Bar Chart
plt.bar(courses, popularity, color =c_pop_color,width = 0.5)

plt.xlabel("Programming Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Languages")
plt.show()
