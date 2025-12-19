import pandas as pd
df = pd.read_csv("Book1.csv")

print(df[['Name','Salary']])
print(df.iloc[2])
print(df.iloc[0,2])
print(df.iloc[:3])
print(df[df['Age'] > 28 ])
print(df[df['Department'] == 'IT' ])

HrData = df[(df['Department'] == 'HR') & (df['Salary'] == 40000)]
print(HrData)