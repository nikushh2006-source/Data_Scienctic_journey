# head()
# tail()
import pandas as pd
df = pd.read_json("Pandas/sample_Data.json")

print("Display top 10 rows;:")
print(df.head(10))

print("Display bottom 10 rows;:")
print(df.tail(10))