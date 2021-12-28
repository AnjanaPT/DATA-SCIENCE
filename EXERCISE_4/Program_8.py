'''8. Given a dataframe, select first 2 rows and output them.'''

import pandas as pd

data = {'RNo' :[15,17,61],
        'Name':['Anjana','Anupama','Elizabeth'],
        'Batch':['Batch1','Batch1','Batch2']}
dataframe = pd.DataFrame(data)
print('----------------------------\nOriginal Dataframe\n----------------------------\n',dataframe)

# Extracting First 2 Rows of the Dataframe
_2_Rows = dataframe.iloc[[0,1]]
print('----------------------------\nExtracting First 2 Rows\n----------------------------\n',_2_Rows)