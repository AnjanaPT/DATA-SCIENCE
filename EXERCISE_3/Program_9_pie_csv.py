"""
9. Write a Python programming to create a pie chart of
gold medal achievements of five most
successful countries in 2016 Summer Olympics.
Read the data from a csv file.
Sample data:medal.csv
country,gold_medal
United States,46
Great Britain,27
China,26
Russia,19
Germany,17
"""

import matplotlib.pyplot as plt
import pandas as pd

df =  pd.read_csv('Pgm9.csv')
Country = df["Country"]
Medal = df["Gold_Medal"]

color=['r','gray','teal','lime','#800040','y']
plt.figure(figsize = (8, 6))

plt.pie(Medal, labels=Country, colors=color, autopct='%1.1f%%')
plt.title("Gold medal achievements of five most successful\n"+"countries in 2016 Summer Olympics")
plt.show()