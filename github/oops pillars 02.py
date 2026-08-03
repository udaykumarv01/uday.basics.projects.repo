# OOPS :- Abstraction ,encapsulation

class mobile :                                        # abstraction
    def camera (self):
        print("camera used to take a picture or making video")
    def phone (self):
        print ("phone is used to make calls")
    def messages (self):
        print("messages used to share a sms") 

mobile=mobile()
mobile.camera()
mobile.phone()
mobile.messages()

class bank_account:                         #encapsulation
    def __init__ (self):
        self.__account ={}
    def acc_number(self,key,value):
        self.__account[key] =value
    def balance(self,amount):
        self.__account= amount
    def debit(self,price):
        if self.__account == price:
            print (f"your debit amount is {price}")
        else:
            print("no amount debited")
B_A=bank_account()
B_A.acc_number("account no " , "sbin")
B_A.balance(1)
B_A.debit("100")

B_A.acc_number("account no" ,"sbin" ) 

class vehicle:
    def start(self):
        print("start and ride")
class bike(vehicle):
    def ride(self):
        print("we can ride")

veh=bike()
print(veh.ride)

