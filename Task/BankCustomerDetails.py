import pandas as pd


class BankCustomerDetails:
    def __init__(self):
        self.customerDetails = {
            "accountNumber": [12352040,12352041,12352042,12352010],
            "customerName" : ["selvakumar","Shakthi","siva","mani"],
            "branch" : ["Tenkasi","Tenkasi","Surandai","Pavoorchtram"]
        }

        self.TransactionDetails = {
            "TransactionID" : ["T001","T002","T003","T004"],
            "accountNumber" : [12352040,12352041,12352040,12352010],
            "type" : ["Deposit","Deposit","WithDraw","Deposit"],
            "amount" : [5000,1000,250,100],
            "charges" : [10,2,0.25,0.10]
        }
    def BankDetails(self):
        customerDetails = pd.DataFrame(self.customerDetails)
        TransactionDetails = pd.DataFrame(self.TransactionDetails)
        merged = TransactionDetails.merge(customerDetails)
        merged["NetAmount"]
        merged = merged.groupby("customerName")["NetAmount"].sum().reset_index()
        print(merged)
if __name__ == '__main__':
    obj = BankCustomerDetails()
    obj.BankDetails()