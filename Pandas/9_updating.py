import pandas as pd
data = {
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','mahesh','jagdish','raj'],
     "Age":[23,45,25,45,34,35,21,33],
     "Salary":[45000,23000,34000,46000,35000,67000,86000,65000],
     "Performance_Score":[76,78,90,95,75,88,87,99]

}
df = pd.DataFrame(data)

print(df)
# .loc[]
# df.loc[row_index,"column_Name"] = New_value
df.loc[0,"Salary"]=60000
print(df)
