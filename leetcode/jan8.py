A=input("enter the consuctive numbers : ")
B=input("enter the consuctive numbers : ")
list_A=[int(x) for x in list(str(A))]
list_B=[int(x) for x in list(str(B))]
a=0
for n in list_A:
    a=a*10+int(n)
b=0
for n in list_B:
    b=b*10+int(n)
rev_B=0
while b>0 :
    rev_B = rev_B*10 + b%10
    b//=10
x=rev_B
rev_A=0
while a>0:
    rev_A= rev_A*10 + a%10
    a//=10
y=rev_A
sum=x+y
result=[int(i) for i in list(str(sum))]
print(f"the list of reversed sum of two list is : {result}")