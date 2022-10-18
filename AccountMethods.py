
from AccountClasses import Account, customer
import random
import csv

fnameCustomer = "customerDB.csv"

def transaction():
    pass

def startmenu():
    print("WELCOME TO THE BANK\n")
    print("Existing Customer Click 1 :\n") 
    print("New Customer Click 2 :\n" ) 
    selection = int(input("Make selection ---->>>  "))
    
    if selection == 1:
        login()
    elif selection == 2:
        newacct()
        login()
    else:
        print("invalid option selected ")
        
    
def login():
    print("Enter the login details of the customer \n")
    AccNum = str(input("Enter your account number ----->>\n"))
    password= input("Enter your password----->> \n")
    checkcusutomer(AccNum,password,fnameCustomer)
    
def newacct():
    print("Welcome New customer to CITIZENS bank\nNew Customer enter your details: \n")
    FirstName= str(input("Enter Customers Firstname ---> \n"))
    LastName= str(input("Enter Customers LastName ---> \n"))
    password= input("Enter your password----->> \n")
    print("Select Account type . \nEnter 1 for Saving \nEnter 2 for Checking \n")
    select = int(input("----->>   "))
    if  select ==1:
        AccNum= generateAccNumSavings()
        type ="Savings"
    elif select==2:
        AccNum=generateAccNumChecking()
        type ="Checking"
    newcustomer= customer(FirstName,LastName,password)
    AccountDetails = Account(AccNum,type,0)
    print("Account has been created\n\n\n")
    savenewcustomer(FirstName,LastName,AccNum,type,password,fnameCustomer)
    print(f"Your Balance is {AccountDetails.balance} \nWould you like to make a deposit right now ? ")
    response = input("Y/N---->>")
    if  response in ("YES","Y","y","yes"):
        deposit= int(input("Enter Amount to Deposit----->>\n"))
        AccountDetails.deposit(deposit)
    else :
        pass
    print(f"welcome New customer {newcustomer.firstname} {newcustomer.lastname} , Your Account number is {AccountDetails.AccNum} Balance is {AccountDetails.balance}")
    print(f"\n\n\n\n\n")
    


def generateAccNumSavings():
    result ="SA"
    for x in range(6):
        value = str(random.randint(0, 9))
        result=result+value
    return result

def generateAccNumChecking():
    result ="CH"
    for _ in range(6):
        value = str(random.randint(0, 9))
        result=result+value
    return result

def savenewcustomer(firstname,lastname,AccountNumber,accountType,password,fname):
    with open(fname,"a") as f:
        f.write(f"{firstname},{lastname},{AccountNumber},{accountType},{password}\n")
        

def checkcusutomer(AccountNumber,Password,fname):
    with open(fname,"r") as f:
        data=csv.reader(f)
        for row in data:
            AccNo= row[2]
            passw = row[4]
            if (AccountNumber ==AccNo and Password == passw):
                print("Login complete ")
    pass
    