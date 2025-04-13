import pandas as pd
import numpy as np
data=pd.read_csv('Friends.csv')
print(data['name'].duplicated().sum())
print(data.drop_duplicates('index'))
if 'salary' in data.columns:
    data["salary"] = data["salary"].replace([10000,np.nan], 500)
if 'city' in data.columns:
    data['city'] = data['city'].replace(np.nan, 'Banglore')
else:
    print("column salary does not exits")

print("Updated DataFrame:")
print(data)
