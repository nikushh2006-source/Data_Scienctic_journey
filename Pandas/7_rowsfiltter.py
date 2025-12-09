import pandas as pd
data = {
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','mahesh','jagdish','raj'],
     "Age":[23,45,25,45,34,35,21,33],
     "Salary":[45000,23000,34000,46000,35000,67000,86000,65000],
     "Performance_Score":[76,78,90,95,75,88,87,99]

}
df = pd.DataFrame(data)

high_salary = df[df["Salary"]>50000 ]
print("Employee with high salary >50000")
print(high_salary)

# filttering salary>50k & Age>30
filter = df[(df['Salary']>50000) & (df['Age'] >30)]
print("Employee that have Age>30 + Salary>50k")
print(filter)

# using OR 
filter_or = df[(df['Age']>35) | (df["Performance_Score"]>90)]
print("Employee who is age >35 or performance_score >90")
print(filter_or)