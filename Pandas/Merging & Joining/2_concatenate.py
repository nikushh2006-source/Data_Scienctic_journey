# '''
# vertically (row-wise)
# horizontally(column wise)

# pd.concat([df1,df2],axis =0,ignore_index=True)
# '''
# import pandas as pd
# # region1
# df_Region1 = pd.DataFrame({
#     'CustomerID':[1,2],
#     'Name':['Gopal','Raju']
# })

# # region2
# df_Region2 = pd.DataFrame({
#     'CustomerID':[3,4],
#     'Name':['Shyam','Baburao']
# })
# # vertically
# df_concat = pd.concat([df_Region1,df_Region2],axis=0,ignore_index=True)
# print(df_concat)

# # horizontally
# df_concat = pd.concat([df_Region1,df_Region2],axis=1,ignore_index=True)
# print(df_concat)
try:
    value = input("Enter a value: ")
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")


