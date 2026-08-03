# functions
print(">>>using positional arguments")
def comparission(man, animal):
    print(f"{man} is like a {animal}")

comparission("yogesh", "donkey")                 # positional arguments

print(">>>using default arguments")
def comparission(man, animal="monkey"):
    print(f"{man} is like a {animal}")

comparission("yogesh")          # default arguments - used when a particular parameter is same for all

print(">>>using key word arguments")
def comparission(man, animal):
    print(f"{man} is like a {animal}")

comparission(man="yogesh", animal="bear")           # key word arguments

def tables(number):
    for i in range(1, 11):
        print(f"{number}x{i} == {number*i}")

tables(25124)

def add(*num):                                      # arg
    return sum(num)

print(add(100,20,1))

def bus_ticket(**details):                          #kwargs
    print(f" type of details {type(details)}")
    for key, value in details.items():
        print(f"{key},{value}")
bus_ticket(gender="male", age=25 ) 
print(f" type of bus_ticket {type(bus_ticket)}")

square_value= lambda x:x**2                         #lambda function
print(square_value(5))

list_weights=[
    {"name": "uday","weight":50},
    {"name":"yogesh","weight":84},
    {"name":"nandan","weight":78}
]
list_weights.sort(key=lambda x:x["weight"],reverse=True )
print(list_weights)

def name(index):                                      #recursion (factorial)
    if index==0:
        return 1
    return index*name(index-1)

print(name(5))

def first_function(name1,name2):                      # nested function
    def second_function():
        print(f"{name1} saying that hey {name2} how are you i know that you are reading python")
    second_function()
first_function("uday","yogesh")




print("thanks for using uday's softwares ")