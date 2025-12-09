# for adding stretforward
import pandas as pd
data = {
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','mahesh','jagdish','raj'],
     "Age":[23,45,25,45,34,35,21,33],
     "Salary":[45000,23000,34000,46000,35000,67000,86000,65000],
     "Performance_Score":[76,78,90,95,75,88,87,99]

}
df = pd.DataFrame(data)

print(df)
print("Adding some bonas on salary")
df["Bonas"]=df['Salary']*0.1
print(df)

# using insert ()
# df.insert(loc,"column_Name",some data)

df.insert(0,"Employee",[10,20,30,40,50,60,70,80])
print(df)