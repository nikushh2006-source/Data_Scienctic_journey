import pandas as pd 
Data = {
    "Name":['Ram' ,'Shyam','Ghanshyam'],
    "Age":[10, 20, 30 ],
     "City": ['Mumbai','Delhi','Nagpur']
}

df = pd.DataFrame(Data)
print("Display the info of data set:")
print(df.info())