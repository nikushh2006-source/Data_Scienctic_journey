# polynominal
import pandas as pd
Data ={
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}
df = pd.DataFrame(Data)
print('Before interpolation:')
print(df)
print('After interpolation:')
df['Value']=df['Value'].interpolate(method='polynomial',order=2)
print(df)
