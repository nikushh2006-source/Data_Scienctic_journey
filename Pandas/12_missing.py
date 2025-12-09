import pandas as pd
data = {
    "Name":['Ram',None,'Ghanshyam','Dhanshyam','Aditi','mahesh','jagdish','raj'],
     "Age":[23,None,25,45,34,None,21,33],
     "Salary":[45000,None,34000,46000,35000,67000,86000,65000],
     "Performance_Score":[76,None,90,95,75,88,87,99]

}
df = pd.DataFrame(data)

print(df)
# find missing number
print(df.isnull())
# sum of missing number 
print(df.isnull().sum())
