"""A code on entering pin code to the bank account/ATM"""
PIN_CODE="987"
a=1
while a<=3:
    x=input(f"trial no:{a} | please enter pin code :- ") 
    a+=1
    if x==PIN_CODE:
        print("entered pincode is correct")
        break
    else :
        print("entered pincode is wrong" )

print("thanks for using uday's softwares ")