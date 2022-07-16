#code for a simple bank management system
class bank: #Class named bank
    
    def __init__(self,name,pan,bday,address,sex,email): #Fucntion for initialization 
        self.name=name
        self.pan=pan
        self.bday=bday
        self.address=address
        self.sex=sex
        self.email=email
        self.balance=0
        
    def account_creation(self): #Function for creating an account 
        print("")
        print("The account has been created successfully,account details given below : ")
        print("Name : {0}".format(self.name))
        print("Account Number : 123456")
        print("PAN Number : {0}".format(self.pan))
        print("Date of Birth : {0}".format(self.bday))
        print("Address : {0}".format(self.address))
        print("Sex : {0}".format(self.sex))
        print("Email : {0}".format(self.email))
        print("")
    
    def deposit(self,d):  #Function for depositing money
        self.d=d
        self.balance=self.balance+self.d
        print("{0} rupees has been deposited into the account successfully".format(self.d))
        print("")
    
    def withdraw(self,w):  #Function for withdrawing money
        self.w=w
        x=self.balance
        x=x-self.w
        
        if x>=0:
            self.balance=x
            print("{0} rupees has been successfully withdrawed from the account".format(self.w))
        else:
            print("Not enough balance")
        print("")
            
    def check_balance(self):  #Function for checking balance in account
        print("The balance in account : {0}".format(self.balance))
        print("")
    
    def transfer_amount(self,ta,tn,t):
        print("")
        self.t=t
        self.ta=ta
        self.tn=tn
        x=self.balance
        x=x-self.t
        
        if x>=0:
            self.balance=x
            print("  //Money has been successfully transfered to the account with details//  ")
            print("   Account Number : {0}".format(self.ta))
            print("   Account Name : {0}".format(self.tn))
            print("   Amount of money transfered : {0}".format(self.t))
        else:
            print("Not enough balance")
        print("")
        
    def search(self,s):  #Function for searching an account detail
        if s=="name":
            print("Name : {0}".format(self.name))
        elif s=="account no":
            print("Account Number : 123456")
        elif s=="pan":
            print("PAN Number : {0}".format(self.pan))
        elif s=="dob":
            print("Date of Birth : {0}".format(self.bday))
        elif s=="address":
            print("Address : {0}".format(self.address))
        elif s=="sex":
            print("Sex : {0}".format(self.sex))
        elif s=="email":
            print("Email : {0}".format(self.email))
        else:
            print("No such detail exists,enter correct value...Try again!!!")
        
        print("")
     
        
#Main code (Menu driven form)    
print("Welcome to the Bank!!!")
print("")

while 1:

    print("a)Account Ceation")
    print("b)Deposit")
    print("c)Withdraw")
    print("d)Check Balance")
    print("e)Transfer Money")
    print("f)Search a particular account detail")
    print("g)Exit")
    print("")
    option=input("Enter the action you want to perform : ")
    
    if option=="a":
        print("")
        print("**ACCOUNT CREATION**")
        name=input("Enter name : ")
        pan=int(input("Enter PAN Number : "))
        bday=input("Enter date of birth(dd/mm/yyyy)(DOB) : ")
        address=input("Enter address : ")
        sex=input("Enter sex(m,f,other) : ")
        email=input("Enter email address : ")
        obj=bank(name,pan,bday,address,sex,email)  #Object creation
        obj.account_creation()
    
    if option=="b":
        print("")
        print("**DEPOSIT**")
        dep=int(input("Enter the amount to be deposited : "))
        obj.deposit(dep)
    
    if option=="c":
        print("")
        print("**WITHDRAW**")
        wid=int(input("Enter the amount to be withdrawed : "))
        obj.withdraw(wid)
        
    if option=="d":
        print("")
        print("**CHECK BALANCE**")
        obj.check_balance()
    
    if option=="e":
        print("")
        print("**TRANSFER AMMOUNT**")
        tao=int(input("Enter the Account number to which money to be transfered : "))
        tn=input("Enter the Name of Account to which money to be transfered : ")
        tranf=int(input("Enter the amount to be transfered : "))
        obj.transfer_amount(tao,tn,tranf)
    
    if option=="f":
        print("")
        print("**SEARCH A PARTICULAR ACCOUNT DETAIL**")
        detail=input("Enter the account detail to be searched (choose from name/account no/pan/dob/address/sex/email) : ")
        obj.search(detail)
        
    if option=="g":
        print("Thank you for using this bank,visit again!!")
        break  
        #The code gets over here

