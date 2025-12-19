import pandas as pd
df = pd.read_csv("Book1.csv")

print(f"The Employee Salary Details:\n{df[['Name','Salary']]}")
print(f"\nThe Third Employee Details:\n{df.iloc[2]}")
print(f"\nThe First Three Employee Details:\n{df.iloc[:3]}")
print(f"\nThe Year Old Employee Details:\n{df[df['Age'] > 28 ]}")
print(f"\nThe IT Department Employee Details:\n{df[df['Department'] == 'IT' ]}")

HrData = df[(df['Department'] == 'HR') & (df['Salary'] == 40000)]
print(f"\nThe HR  With 40000 Salary:\n{HrData}")