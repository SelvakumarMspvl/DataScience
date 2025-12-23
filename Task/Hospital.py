import pandas as pd

df = pd.read_csv("D:\selvakumar\DataScience\Task\ExcelFiles\Hospital.csv")

print("patients Details:\n",df[["Name","Department"]])
print("The bill amounts:\n",df.iloc[:,5])
print("patients above 50 age: \n",df[df["Age"] > 50])
print("patients bill above 10000 Rs: \n",df[df["Bill"] > 10000])
print("patients bill above 10000 Rs in Cardiology: \n",df[(df["Bill"] > 10000) & (df["Department"] == "Cardiology")])
print("Selecting alternate rows:\n",df.iloc[::2])

print("Missing values:\n",df.isnull())
print("Count Missing values:\n",df.isnull().sum())
print("Rows with Missing values:\n",df[df.isnull().any(axis = 1)])
print("Dropped missing row: \n",df.dropna())

df["Bill"].fillna(df["Bill"].mean(),inplace = True)
df["Age"].fillna(df["Age"].mean(),inplace = True)
print("Filled Age and Bill\n",df)
print(df["Name"].mode(),"\t",df["City"].mode())
df["City"].fillna(method="ffill",inplace = True)
print(df)
print("Average Bill amount: ",df["Bill"].mean())

Mean = df["Bill"].mean()
df["Boolean_flag"] = df["Bill"] > Mean
print(df)

print(df["Department"].value_counts())

print(df[(df["City"] == "Coimbatore") & (df["Department"] == "Neurology")])

print(df.sort_values( by = "Bill" ,ascending = False).head(3))