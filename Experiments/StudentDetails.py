class StudentDetails:
    def __init__(self):
        self.Student = {
            "Roll_no":[],
            "name":[],
            "department":[],
            "Percentage":[]
        }
        self.defaultDepartment = ["Computer","IT"]

    # This Function Get The Input From The User
    def getStudentDetails(self,how):
        for i in range(how):
            # Roll no Getting
            print("\nStudent no: ",i+1)
            roll_no = input("Enter The Roll Number Of The Student: ")
            while not roll_no.isdigit():
                roll_no = input("Enter The Valid Roll Number Of The Student: ")
            self.Student["Roll_no"].append(roll_no)
            # Name Getting
            name = input("Enter The Name Of The Student: ")
            while not name.isalpha():
                name = input("Enter The Correct Name Of The Student: ")
            self.Student["name"].append(name)
            # Department Getting
            dept =  input("Enter The Department Of The Student: ")
            while not dept in self.defaultDepartment:
                dept = input("Enter The Correct Department Of The Student (Computer/IT): ")
            self.Student["department"].append(dept)
            # Percentage Getting
            percentage = input("Enter The Last Exam Mark Percentage Of The Student: ")
            self.validatePercentage(percentage)

    # Function For Validate The Percentage
    def validatePercentage(self,percentage):
        if percentage.isdigit():
            percentage = int(percentage)
            if percentage < 0 or percentage > 100:
                percentage = input("Enter The Last Exam Mark Percentage Correctly : ")
                self.validatePercentage(percentage)
            self.Student["Percentage"].append(percentage)
        else:
            percentage = input("Enter The Last Exam Mark Percentage Correctly: ")
            self.validatePercentage(percentage)

    # Function For Print The Student Details
    def printStudentDetails(self):
        print("            2025 Model Exam Mark List")
        print("+--------------------------------------------------+")
        print("Roll No\t\tStudent Name\t\tDepartment\t\tPercentage")
        for i in range(0,len(self.Student['Roll_no'])):
            print(
                f"{self.Student['Roll_no'][i]}\t\t"
                f"{self.Student['name'][i]}\t\t"
                f"{self.Student['department'][i]}\t\t"
                f"{self.Student['Percentage'][i]}%"
            )
        print("+--------------------------------------------------+")

    # This Function Handel The Flow Of Program
    def Main(self):
        how = int(input("Enter the How Many Student Record Want To Enter: "))
        self.getStudentDetails(how)
        self.printStudentDetails()

if __name__ == "__main__":
    obj = StudentDetails()
    obj.Main()