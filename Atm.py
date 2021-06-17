class Atm:
    def __init__(self):
        self.balance=50000
        print("Hello! Welcome to the Atm")
        self.cardNum=input("Please Enter your Card number and press enter-")
        self.pinNum=input("Please Enter your Pin number and press enter-")


  
    def Belence(self):
        
        print("\n Belence Available-",self.balance)
  
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn-"))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew-", amount)
        else:
            print("\n Insufficient balance")
  
    def updateBelence(self):
        print("\n Available Balance-",self.balance)
  

   

s = Atm()
   

s.Belence()
s.withdraw()
s.updateBelence()