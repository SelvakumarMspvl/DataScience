import pandas as pd
dataFrame =  pd.read_csv("Book1.csv")

print("The orginial data is: \n",dataFrame)
nullValue = dataFrame.isnull().sum()
print("The missing data count are: ", nullValue)

dataFrame["mark1"] = dataFrame["mark1"].fillna("Absent")
dataFrame["mark2"] = dataFrame["mark2"].fillna(0)

print("After the data process:\n",dataFrame)
