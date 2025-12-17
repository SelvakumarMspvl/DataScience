class TeaShop:
    def __init__(self):
        self.customerName = None
        self.products = {
            1:["Tea  ",10],
            2:["vadai",7],
            3:["Buffs",15]
        }
        self.selectedProduct = []
        self.qty = []
        self.BillAmount = []
        self.TotalAmount = 0
    def Menu(self):
        self.customerName = input("Enter The Your Name :")
        print("+------- Our Products -------+")
        print("S.no\tItems\t\tPrice")
        for i in range(1,len(self.products)+1):
            print(f"{i}\t\t{self.products[i][0]}\t\t{self.products[i][1]}")
        print("+----------------------------+")
        self.selectedProduct = list(map(int,input("Select Your Option :").split()))
        self.qty = list(map(int,input("Enter the Qty:").split()))
        self.CreateBill()
    def CreateBill(self):
        for i in range(len(self.selectedProduct)):
            amount = self.products[self.selectedProduct[i]][1] * self.qty[i]
            self.TotalAmount += amount
        self.PrintBill()
    def PrintBill(self):
        print("\n              SSK Coffee Park")
        print("Customer Name: ",self.customerName)
        print("+------------ Your Bill ------------+")
        print("S.no\tItems\tQty\t\tPrice")
        for i in range(len(self.selectedProduct)):
            print(f"{i+1}\t\t{self.products[self.selectedProduct[i]][0]}\t {self.qty[i]}\t\t{self.products[self.selectedProduct[i]][1]}")
        print("+------------------------------------+")
        print("\t\t\t\tTotal Bill Amount: ",self.TotalAmount)
        print("         Thanking you for ordering")
if __name__ == "__main__":
    obj = TeaShop()
    obj.Menu()