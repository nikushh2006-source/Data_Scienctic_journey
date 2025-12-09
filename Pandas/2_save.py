import pandas as pd 
Data = {
    "Name":['Ram' ,'Shyam','Ghanshyam'],
    "Age":[10, 20, 30 ],
     "City": ['Mumbai','Delhi','Nagpur']
}

df = pd.DataFrame(Data)
print(df)

# df.to_csv("output.csv", index=False)
# df.to_json("output.json" ,index=False)
df.to_excel("output.xlsx" , index=False)