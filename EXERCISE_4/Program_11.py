'''11. Given  is  a  dataframe  showing  Company  Names  (cname)  and  corresponding  Profits (profit).  Convert the  values  of  Profit  column  such that  values  in  it  greater than  0  are set to True and the rest are set to False.'''

import pandas as pd


data = {'CName':['TCS','Wipro','Cognizant','Infosys','UST Global'],
        'Profit':[10000,-1000,60000,20000,-20000]
       }
C_dataframe = pd.DataFrame(data)
print('------------------------------------\nOriginal Dataframe\n------------------------------------\n',C_dataframe)

C_dataframe['Profit'] = C_dataframe['Profit'].apply(lambda x:x>0)
print('------------------------------------\nTrue Or False(Profit)\n------------------------------------\n',C_dataframe)
