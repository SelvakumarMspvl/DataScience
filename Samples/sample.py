import pandas as pd

orders = {
    "orderId" : [2101,2102,2103,2104],
    "customerId" : ['c11','c12','c13','c11'],
    "restaurant" : ['A2B Veg','BBQ Nation','Pizza Hub','A2B Veg'],
    "foodItem" : ['Dosa','Grill Chicken','Cheese Pizza','Idly'],
    "quantity" : [3,1,2,5],
    "price" : [40,350,250,15],
    "deliveryFee" : [20,30,25,20]
}

customer = {
    "customerId" : ['c11','c12','c13','c14'],
    "CustomerName" : ['vimal','Nisha','Arvind','Kavitha'],
    "area" : ['Anna Nagar','Velachery','Tambaram','Porur']
}

order_df = pd.DataFrame(orders)
customer_df = pd.DataFrame(customer)
order_df["Total"] = order_df["quantity"] * order_df["price"]

print("\t\tThe Customer Order History")
print("+---------------------------------------------------------------------+")
print((order_df.merge(customer_df, how = 'left' , on = "customerId")))
print("+---------------------------------------------------------------------+")


merged = order_df.merge(customer_df, how='right', on="customerId")
merged.groupby("customerId")
print("\t\tThe Customer Order History")
print("+---------------------------------------------------------------------+")
print(merged)
print("+---------------------------------------------------------------------+")