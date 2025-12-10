import calendar

name = str(input("enter your name : "))
year = int(input("enter your year of birth : "))
# please enter your birth year
month = int(input("enter your month of birth : "))
# please enter your birth month
print(calendar.month(year, month))
# you get calendar of your birth month