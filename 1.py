boy_name=input("boy name : ")

girl_name= input("girl name : ")

boy_age = int(input ("boy age : "))

girl_age=int(input("girl age : "))
# abs because some times girl age is may be greater threrfore not represnt negative value
# abs means absolute value
age_diff= abs(boy_age - girl_age)
print (age_diff)

print(f"{boy_name} loves {girl_name}, and their age diffrence is {age_diff}")

""" use for multi line comments """