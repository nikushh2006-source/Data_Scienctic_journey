'''
df["column Name"].mean()
df["column Name"].max()
df["column Name"].min()
df["column Name"].sum()
'''
import pandas as pd
Data = {
    "Name":["Varun","Tarun","Karun"],
    "Age":[23,43,33],
    "Salary":[100000,400000,500000]
}
df= pd.DataFrame(Data)
avg_Salary = df["Salary"].mean()
print(avg_Salary)
min_Salary = df["Salary"].min()
print(min_Salary)
max_Salary = df["Salary"].max()
print(max_Salary)
sum_Salary = df["Salary"].sum()
print(sum_Salary)