from idlelib.query import CustomRun

import pandas as pd
class MyCompany:
    def __init__(self):
        self.Sale_data = {
            "TransactionID" :["TSK10001","TSK10002","TSK10003"],
            "CustomerID" :["Csk101","Csk102","Csk101"],
            "ProductName": ["pen","mouse","Scale"],
            "Qty":[2,1,4],
            "Price":[10,500,5]
        }
        self.customer_Data = {
            "CustomerID" : ["Csk101","Csk102","Csk103","Csk104","Csk105"],
            "CustomerName" :["selvakumar","ShakthiGanesh","siva","Mathi","Mathavan"],
            "CustomerCity": ["Tenkasi","Tenkasi","Tenkasi","Tenkasi","Tenkasi"],
            "Phone Number": [8940271739,9565251542,9568253515,9568253515,9568253515],
        }
    def mainFunction(self):
        my_list = ["left","right","inner","outer"]
        for i in my_list:
            print("\n         ",i," Join")
            Salse_df = pd.DataFrame(self.Sale_data)
            Customer_df = pd.DataFrame(self.customer_Data)
            merged = Salse_df.merge(Customer_df, how = 'left' , on = "CustomerID")
            merged["Total"] =merged["Qty"] * merged["Price"]
            merged = merged.groupby("CustomerName")["Total"].sum().reset_index()
            print(merged)





if __name__ == "__main__":
    obj = MyCompany()
    obj.mainFunction()