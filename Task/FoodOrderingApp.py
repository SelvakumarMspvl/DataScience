import pandas as pd
from pandas import merge


class FoodOrderingApp:
    def __init__(self):
        self.orders = {
            "orderId" : [2101,2102,2103,2104],
            "customerId" : ['c11','c12','c13','c11'],
            "restaurant" : ['A2B Veg','BBQ Nation','Pizza Hub','A2B Veg'],
            "foodItem" : ['Dosa','Grill Chicken','Cheese Pizza','Idly'],
            "quantity" : [3,1,2,5],
            "price" : [40,350,250,15],
            "deliveryFee" : [20,30,25,20]
        }

        self.customer = {
            "customerId" : ['c11','c12','c13','c14'],
            "CustomerName" : ['vimal','Nisha','Arvind','Kavitha'],
            "area" : ['Anna Nagar','Velachery','Tambaram','Porur']
        }

        self.order_df = None
        self.customer_df = None

    def processData(self):
        self.order_df = pd.DataFrame(self.orders)
        self.customer_df = pd.DataFrame(self.customer)
        self.order_df["Total"] = (self.order_df["quantity"] * self.order_df["price"]) + self.orders["deliveryFee"]

    def display(self):
        print("\t\tThe Customer Order History")
        print("+---------------------------------------------------------------------+")
        print((self.order_df.merge(self.customer_df, how = 'left' , on = "customerId")))
        print("+---------------------------------------------------------------------+")

        merged = self.customer_df.merge(self.order_df, how='left', on="customerId")
        merged.groupby("customerId")["Total"].sum().reset_index()

        merged.to_csv("sample.csv")

        print("\t\tThe Customer Order History")
        print("+---------------------------------------------------------------------+")
        print(merged)
        print("+---------------------------------------------------------------------+")

    def main(self):
        self.processData()
        self.display()

if __name__ == '__main__':
    obj = FoodOrderingApp()
    obj.main()