# pd.merge(df1,df2,on="Column_name", how="type of join")
import pandas as pd 

# customer dataframe
df_customer =pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':["Ramesh","Suresh","Kalpesh"]
})
# order dataframe
df_order= pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmount':[250,450,350]
})

# merge(inner)
# df_merged= pd.merge(df_customer,df_order,on="CustomerID",how="inner")
# print("inner join")
# print(df_merged)
# merge(outer)
# df_merged= pd.merge(df_customer,df_order,on="CustomerID",how="outer")
# print("outer join")
# print(df_merged)
# right merge
# df_merged= pd.merge(df_customer,df_order,on="CustomerID",how="right")
# print("right join")
# print(df_merged)

# left merge
# df_merged= pd.merge(df_customer,df_order,on="CustomerID",how="left")
# print("left join")
# print(df_merged)

# cross merge
df_merged= pd.merge(df_customer,df_order,how= "cross")
print("cross join")
print(df_merged)
'''
cross merge
1df= m rows
2df = n rows
m*n rows
'''