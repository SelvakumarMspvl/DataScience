import pandas as pd
df = pd.read_csv("D:\selvakumar\DataScience\Task\ExcelFiles\DataTransformation.csv")
print("Records Without Duplicates:\n", df.drop_duplicates())

print("\nReplacing Department and Grade:\n",df.replace({
    "X": "C",
    "Finance" : "Fin"
}))

print("\t\t\tSummary\n")
print("\nCount Of Employee:\n",df.groupby("Dept")["EmpId"].count())

print("\nAverage Salary In Each Department:\n", df.groupby("Dept")["Salary"].mean())

print("\nThe Maximum and Minimum Salary In The Data Set Is:\n",df.groupby("Dept")["Salary"].aggregate(["min","max"]))

print("\n The Average Of Age Is:\n",df.groupby("Dept")["Age"].mean())

