import pandas as pd
import numpy as np


studentDataFrame = pd.read_csv("Book1.csv")
print(f"The Minimum Value:\n{studentDataFrame.min()}")
print(f"\n\nThe Maximum Value:\n{studentDataFrame.max()}")
print(f"\n\nThe CumSum Value:\n{studentDataFrame.cumsum()}")
print(f"\n\nThe Average: {studentDataFrame['mark1'].mean()}")
print(f"\nThe Median: {studentDataFrame['mark1'].median()}")
print(f"\nThe Standard Division: {studentDataFrame['mark1'].std()}")
print(f"\nThe Co-Efficient {np.corrcoef(studentDataFrame['mark1'],studentDataFrame['mark2'])}")