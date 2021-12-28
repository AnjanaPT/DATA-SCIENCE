'''4. Given a 2D List, convert it into corresponding dataframe and display it'''

#program 4

import pandas as pd

_2D_list = [['Anjana',15,'Batch1'],
            ['Anupama',17,'Batch1'],
            ['Elizabeth',61,'Batch2']]

dataframe = pd.DataFrame(_2D_list, columns = ['Name','RNo','Batch'])

print(dataframe)