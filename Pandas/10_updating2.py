import pandas as pd
data = {
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','mahesh','jagdish','raj'],
     "Age":[23,45,25,45,34,35,21,33],
     "Salary":[45000,23000,34000,46000,35000,67000,86000,65000],
     "Performance_Score":[76,78,90,95,75,88,87,99]

}
df = pd.DataFrame(data)

print(df)
# increasing salary 5%
df["Salary"] = df["Salary"]*1.05
print(df)