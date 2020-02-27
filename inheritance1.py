class COUNTRY():
    def __init__(self,language,capital,country):
        self.language = language
        self.capital = capital
        self.country = country

    def detail(self):
        print("the country is ",self.country)

class status(COUNTRY):
    def __init__(self,language,capital,country):
        COUNTRY.__init__(self,language,capital,country)

        self.country = (self.country).upper()

    def detail(self):
        if self.country =="NEPAL":
            print("the country is under developing ","and the language spoken is ",self.language)
        else:
            print("the country America is develokped ", "and the language sopken is ",self.language)
# # to print country status of NEpal and America is it developing or not developed

a = (input("enter country either Nepl or America : "))
b =(input("enter language spoken : "))
c = (input("Enter capital city : "))
n = status(b,c,a)
n.detail()
