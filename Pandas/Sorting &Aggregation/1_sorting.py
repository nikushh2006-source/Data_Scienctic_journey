# sorting data
# SORTING DATA in1 column sort_values()
# df.sort_values(by="Columns Name",True\False, inplace = True)
import pandas as pd
Data = {
    "Name":["Varun","Tarun","Karun"],
    "Age":[23,43,33],
    "Salary":[100000,400000,5000000]
}
df= pd.DataFrame(Data)
df.sort_values(by="Age",ascending=False,inplace=True)
print('Sorted by Accending oder:')
print(df)