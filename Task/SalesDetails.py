import pandas as pd

dataFrame = pd.read_csv("D:\selvakumar\DataScience\Task\ExcelFiles\SalesDataset.csv")

print(
    f"The Customer Category Details:\n"
    f"{dataFrame[['CustomerName','Category']]}"
)
print(
    f"The Quantity Column With Category:\n"
    f"{dataFrame.iloc[1,3]}"
)
print(
    f"The Details About purchase More Then 2 Products:\n"
    f"{dataFrame[dataFrame['Quantity'] > 2]}"
)
print(
    f"The Details About purchase More Then 25000 Rs Products:\n"
    f"{dataFrame[dataFrame['Price'] > 25000]}"
)
print(
    f"The Details About purchase In Electronics More Then 30000 Rs Product:\n"
    f"{dataFrame[(dataFrame['Category'] == 'Electronics') & (dataFrame['Price'] > 30000)]}"
)
print(
    f"The Alternating printing:\n"
    f"{dataFrame.iloc[::2]}"
)

dataFrame["totalAmount"] = dataFrame['Quantity'] * dataFrame['Price']
print(
    f"The Details About purchase Totally More Then 60000 Rs Product"
    f"{dataFrame[dataFrame['totalAmount'] > 60000]}"
)
print(
    f"The Details About purchase In Electronics From South Region:\n"
    f"{dataFrame[(dataFrame['Category'] == 'Electronics') & (dataFrame['Region'] == 'South')]}"
)
print(
    f"Region Count:\n"
    f"{dataFrame['Region'].value_counts()}"
)
print(
    f"High Value Customer are:\n"
    f"{dataFrame.sort_values('Price',ascending=False).head(3)}"
)