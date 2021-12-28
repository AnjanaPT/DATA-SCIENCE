'''3. Given a dictionary, convert it into corresponding dataframe and display it'''

import pandas as pd

dictionary = {'Name':['Anjana','Anupama','Elizabeth'],
              'RNo' :[15,17,61],
              'Batch':['Batch1','Batch1','Batch2']}


dataframe = pd.DataFrame(dictionary)

print(dataframe)