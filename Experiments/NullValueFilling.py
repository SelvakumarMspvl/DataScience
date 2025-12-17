import pandas as pd
dataFrame =  pd.read_csv("Book1.csv")

print("The orginial data is: \n",dataFrame)
print("The missing data count are: ", dataFrame.isnull().sum())

dataFrame["mark1"] = dataFrame["mark1"].fillna(0)
dataFrame["mark2"] = dataFrame["mark2"].fillna("Absent")

print("After the data process:\n",dataFrame)
