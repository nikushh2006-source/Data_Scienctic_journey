# df.sort_values(by=["Age","Salary"],ascending = [True,False],inplace=True)
import pandas as pd
Data = {
    "Name":["Varun","Tarun","Karun"],
    "Age":[23,43,33],
    "Salary":[100000,400000,500000]
}
df= pd.DataFrame(Data)
df.sort_values(by=["Age","Salary"],ascending=[True,False],inplace=True)
print('Sorted by Accending oder:')
print(df)