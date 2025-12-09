import pandas as pd
Data = {
    "Name":["Varun","Tarun","Karun","Tinsu","Sarun"],
    "Age":[28 ,34,22,34,28],
    "Salary":[10000,40000,50000,65000,54000]
}
df= pd.DataFrame(Data)
grouped=df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)
