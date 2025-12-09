# linear
import pandas as pd
Data ={
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}
df = pd.DataFrame(Data)
print('Before interpolation:')
print(df)
print('After interpolation:')
df['Value']=df['Value'].interpolate(method='linear')
print(df)

"""
1-timer series data
2-numeric data with trends
3-avoid droping rows
"""
