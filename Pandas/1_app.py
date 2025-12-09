import pandas as pd
# read data file in csv in dataframe
# df = pd.read_csv("Pandas/sales_data_sample.csv" , encoding="latin1")
df = pd.read_json("Pandas/sample_Data.json")
print(df)