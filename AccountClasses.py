
class customer:
    def __init__(self,firstname,lastname,password) -> None:
        self.firstname = firstname
        self.lastname =lastname
        self.password = password
    
    def __str__(self) -> str:
        return f"Name:" + self.firstname + " " + self.lastname 

    
class Account(customer):
    def __init__(self,AccNum,AccType,balance) -> None:
        super().__init__(firstname,lastname,password)
        self.AccNum = str(AccNum)
        self.AccType=str(AccType)
        self.balance=int(balance)
    
    def __str__(self) -> str:
        return f"Account Number:{self.AccNum} \nAccount Type :{self.AccType} \nAccount Balance: {self.balance}"
    
    def getbalace(self):
        return self.balance
    
    
    def deposit(self,amount):
        self.balance= self.balance+amount
    
    

#create customer class 
#create account class 
#create log in 
#
#
