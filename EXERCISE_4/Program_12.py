'''12. Given are 2 dataframes, with one dataframe containing Employee ID (eid), Employee Name (ename) and Stipend (stipend) and the other dataframe containing Employee ID (eid) and designation of the employee (designation). Output the Dataframe containing Employee   ID   (eid),   Employee   Name   (ename),   Stipend   (stipend)   and   Position (position).'''


import pandas as pd

edata = {'Eid':['E1','E2','E3','E4'],
        'Name':['Anjana','Anupama','Elizabeth','Adham'],
        'Stipend':[35000,40000,40000,30000]}
e_dataframe = pd.DataFrame(edata)
print(e_dataframe,'\n') # 1st DataFrame containing employee id (eid), employee name (ename) and stipend

ecdata = {'Eid':['E1','E2','E3','E4'],
        'Position':['SoftWare Engineer','Data Analyst','Data Scientist','SoftWare Engineer']}
ec_dataframe = pd.DataFrame(ecdata)

print(ec_dataframe,'\n') # 2nd DataFrame containing employee id (eid) and designation of the employee (position)

dataframe = pd.merge(e_dataframe, ec_dataframe, how = 'inner', on = 'Eid') # required dataframe

print(dataframe)