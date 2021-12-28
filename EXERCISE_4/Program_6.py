'''6. Given a dataframe, sort it by multiple columns.'''

#Program 6

import pandas as pd

_2D_list = [['Anupama',17,'Batch1'],
            ['Elizabeth',61,'Batch2'],
            ['Anjana',15,'Batch1']
            ]

dataframe = pd.DataFrame(_2D_list, columns = ['Name','RNo','Batch'])


print('----------------------------\nOriginal Dataframe\n----------------------------\n',dataframe)
# original dataframe


dataframe_sorted = dataframe.sort_values(by = ['Name','RNo','Batch']) # dataframe after sorting by 'id' and 'age'

print('\n----------------------------\nAfter Sorting\n----------------------------\n',dataframe_sorted) 