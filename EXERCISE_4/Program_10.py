'''10. Given a dataframe with NaN Values, fill the NaN values with 0.'''


import pandas as pd
import numpy as np


data = {'Name':['Anjana','Anupama','Elizabeth','Adham'],
        'Occupation':['SoftWare Engineer','Data Analyst','Data Scientist','SoftWare Engineer'],
        'Salary':[np.nan,30000,40000,np.nan]}
dataframe = pd.DataFrame(data)

#Original
print('------------------------------------\nOriginal Dataframe\n------------------------------------\n',dataframe)

#After Filling NaN Values with 0
dataframe_NaN_Fill = dataframe.fillna(0)
print('------------------------------------\nAfter Filling NaN Values with 0\n------------------------------------\n',dataframe_NaN_Fill) 