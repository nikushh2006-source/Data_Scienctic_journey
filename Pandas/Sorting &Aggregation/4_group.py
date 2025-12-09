import pandas as pd
Data = {
    "Name":["Varun","Tarun","Karun","Tarun","Sarun"],
    "Age":[28 ,34,22,34,28],
    "Salary":[10000,40000,50000,65000,54000]
}
df= pd.DataFrame(Data)
grouped=df.groupby("Age")["Salary"].sum()
print(grouped)

'''
df.groupby("Age")
Age = 22 >[50000]
Age = 28 [10000,54000]
Age = 34[40000,65000]

["Salary"].sum()
Age = 22 >[50000]=50000
Age = 28 [10000,54000]=64000
Age = 34[40000,65000]=105000
'''

