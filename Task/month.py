class Month:
    def __init__(self):
        self.ch = None

    def getMonthNmae(self,choise):
        """It Return The Name Of The Month"""
        month = ("January","February","March","April","May","June","July","August","September","October","November","December")
        self.ch = int(self.ch)
        return month[self.ch - 1]

    def getUserInput(self):
        """It Get The User In Put From The User"""
        self.ch = input("Enter The Number To Display The Month: ")
        return self.ValidateUserInput()

    def ValidateUserInput(self):
        """This Function I validate The User Input"""
        if self.ch.isdigit():
            """It cheK the value is Digit Are another Value"""
            while int(self.ch) <= 0 or int(self.ch) > 12:
                self.ch = input("Enter The Number 1 -12 To Display The Month: ")
                if not self.ch.isdigit():
                    self.ValidateUserInput()
            if self.ch.isdigit():
                return self.ch
            else:
                self.ValidateUserInput()
        else:
            """If The Value Is Not A Integer Then It Execute"""
            self.ch = 0
            self.ch = input("Enter The \"INTEGER NUMBER\" 1 -12 To Display The Month: ")
            self.ValidateUserInput()

    def Main(self):
        try:
            """This Control The Flow Of Program"""
            ch = self.getUserInput()
            month = self.getMonthNmae(ch)

            print("You Selected Month Name Is: ", month)
        except KeyboardInterrupt:
            print("\n\nThanks for Using Me!")
if __name__ == "__main__":
    obj = Month()
    obj.Main()