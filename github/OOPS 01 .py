#  OOPS , CLASSES , OBJECTS , CONSTRUCTORS ,

class computer :
    def __init__(self ,comp_name , storage ,Ram ,gen):
        self.comp_name=comp_name
        self.storage=storage
        self.Ram=Ram
        self.gen=gen
    def about(self):
        print(f"'{self.comp_name}' is the company of the computer it has '{self.storage}' storage, it has '{self.Ram}'GB ram, and '{self.gen}'th genration.")
dell =computer("DELL", "1TB", "8","14")
HP = computer("HP" ,"512","16" , "13")
macbook = computer("MAC" , "1TB" ,"16" , "14")

dell.about()
HP.about()
macbook.about()
