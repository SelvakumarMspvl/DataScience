import pandas as pd
import numpy as np


studentDataFrame = pd.read_csv("StudentDataCsv.csv")
print("The Given Data Frame is: \n",studentDataFrame)
print(f"\n\nThe Minimum Value in The Student List Is:\n{studentDataFrame.min()}")
print(f"\n\nThe Maximum Value in The Student List Is:\n{studentDataFrame.max()}")
print(f"\n\nThe CumSum Value of The Student List Is:\n{studentDataFrame.cumsum()}")
print(f"\n\nThe Average of The Subject 1 List Is: {studentDataFrame['Subject1'].mean()}")
print(f"\nThe Median of The Subject 1 Is: {studentDataFrame['Subject1'].median()}")
print(f"\nThe Standard Division of The Subject 1 Is: {studentDataFrame['Subject1'].std()}")
print(f"\nThe Co-Efficient of The Student List Is: \n{np.corrcoef(studentDataFrame['Subject1'],studentDataFrame['Subject2'])}")

