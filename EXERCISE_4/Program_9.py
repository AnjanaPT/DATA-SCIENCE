'''9. Given  is  a  dataframe  showing  name,  occupation,  salary  of  people.  Find  the  average salary per occupation.'''


import pandas as pd

data = {'Name':['Anjana','Anupama','Elizabeth','Adham','Vedha','Gaya'],
        'Occupation':['SoftWare Engineer','Data Analyst','Data Scientist','SoftWare Engineer','Data Analyst','Data Scientist'],
        'Salary':[30000,30000,40000,60000,20000,30000]}
dataframe = pd.DataFrame(data)

print('------------------------------------\nOriginal Dataframe\n------------------------------------\n',dataframe)

#Average Salary Per Occupation
Avg_Slry_Per_Ocptn = dataframe.groupby('Occupation')['Salary'].mean()
print('------------------------------------\nAverage Salary Per Occupation\n------------------------------------\n',Avg_Slry_Per_Ocptn)
