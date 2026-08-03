# a simple code on using the oops concepts in addressing the books datails
class books :
    def __init__ (self ,book_name,original_price,percent):
        AUTHORS={ "billionairs mindsets":"UDAY KUMAR V",
                 "don't trust your body" :"KIRAN" ,
                 "aims of every souls":"PREM KUMAR",
                 "story of kantara":"HEMANTH"
                }
        self.book_name=book_name
        self.AUTHORS=AUTHORS.get(book_name)
        self.book_name=book_name
        self.original_price=original_price
        self.percent=percent
   # calling function to get information about book
    def book_info(self):
        print(f"TITLE: '{self.book_name}'" )
        print(f"AUTHOR : '{self.AUTHORS}'")
        print(f"ORIGINAL PRICE : {self.original_price}₹")
    # calling a function to reduce the price by giving discount
    def discount_price (self):
        # to reduce the original price into discount price to make custmer happy
        print(f"discount = {percent} %")
        print(f"selling_price= {self.original_price -self.original_price*self.percent/100} ₹")    

book_name=str(input("enter the book name : "))
original_price=int(input(f"enter the price of '{book_name}': "))
if original_price<=500:
    percent=10
elif original_price<=1000:
    percent=15
else:
    percent=20
book=books(book_name ,original_price,percent)
book.book_info()
book.discount_price()