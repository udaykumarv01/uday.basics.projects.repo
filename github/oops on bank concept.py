 # code on bank account's owner and them balance and amount credit and debit and total balance
 
class bank_account ():

    def __init__ (self,acc_no,balance=0,credit=0,debit=0):
                
        owners={ 2025000121:"UDAY KUMAR V",
                 2025000122 :"KIRAN" ,
                 2025000123:"PREM KUMAR",
                 2025000124:"HEMANTH"
                }
        self.acc_no=acc_no
        self.owner=owners.get(acc_no)
        self.__balance= balance
        self.credit=credit
        self.__debit=debit

    def credit(self,credits=0):
        if credits>=0:
            self.balance += credits
        else:
            print("you can't add the negative money to your bank account ")

    def debit(self,debits=0):
                        
        if debits>=0:
            if debits<=self.balance:
                self.__balance-=debits
            else:
                print(f"your don't have balance of {debits}")
        else:
            print("you can't take negative money from your bank account")
    def bank_balance(self):
        print(f" Intial bank balance is : {self.__balance}")
        print(f"\n    Account holder name : {self.owner} \n    credited amount : {self.credit} \n    debited amount: {self.__debit}\n    bank balance : {self.credit - self.__debit + self.__balance } ")
acc_no=int(input("enter the account number : "))
credits=int(input(" enter the credit amount : "))
debits=int(input(" enter the debit amount : "))
Account=bank_account(acc_no,0,credits,debits)
Account.bank_balance() 
    
        