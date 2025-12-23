import pandas as pd
df = pd.read_csv('studentDetails.csv')
print("Missing count: \n",df.isnull().sum())
df["Age"] = df["Age"].fillna(df["Age"].mean())
print("Filling Missing Age: \n",df)
df["Marks"] = df["Marks"].fillna(0)
print("Filling Missing Mark: \n",df)

df["Department"] = df["Department"].fillna("Unknown")
print("Filling Missing Department: \n",df)

print(df.drop("Email",axis=1,inplace = True))
print("Delete Missing Column: \n",df)
