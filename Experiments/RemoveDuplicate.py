import pandas as pd

FirstBookDataFrame = pd.read_csv("FirstBook.csv")
SecondBookDataFrame = pd.read_csv("SecondBook.csv")

compained = pd.concat([FirstBookDataFrame,SecondBookDataFrame]).reset_index(drop = True)
print("The compained Data is: \n",compained)

compained = compained.drop_duplicates()

print("After Removing The Duplicate value: \n",compained)