# A project on farmers get bill in diary 
print('hakkinalu haalu huthpadakara sahakari sanga')
input("DATE: ")
input("SHIFT : ")
codes={1:"Venkatarangaiah C",
       2:"Lakshmi narassamma",
        3:"Rakshitha V",
         4:"Pallavi V",
          5:"Uday kumar V" }
X=input("CODE : ")
x=int(X)
a=codes[x]
print(f"Name of farmer: {a}")

b=float(input("volume(l): "))

c=float(input("fat(%): "))
amount= c*9.78
print(f"amount(rup/l):{amount}")
total_amount=amount*b
print(f"Total amount:{total_amount}")
print("thanks to visit")

print("thanks for using uday's softwares")