'''7. Given  a dataframe  with  custom  indexing,  convert  and  it  to  default  indexing  and display it.'''

import pandas as pd

data = {'RNo': [15, 17, 61],
        'Name': ['Anjana', 'Anupama', 'Elizabeth'],
        'Batch': ['Batch1', 'Batch1', 'Batch2']}
dataframe = pd.DataFrame(data)

# custom index
dataframe_customindex = dataframe.set_index('RNo')
print('----------------------------\nCustom Index\n----------------------------\n', dataframe_customindex)

dataframe_defaultindex = dataframe_customindex.reset_index()
print('----------------------------\nDefault Index\n----------------------------\n', dataframe_defaultindex)

