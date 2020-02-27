# success = False
# while success == False:
#
#     try :
#         radius = int(input("enter radius r : "))
#         area = 3.14*(radius)**2
#         print(area)
#         success = True
#     except:
#         print("invalid value for radius")

#crate a function divided with two parameter a,b
#now it should return the divided value like a/b,
#now if the input form the user ie. b = 0 , our program should produce a nice exception error,

def d(a,b):
    print(a/b)


success = False
while success == False:
        try:
            a = int(input("enter a num : "))
            b = int(input("enter a num : "))
            d(a,b)
            success = True
        except:
            print("f*** wrong num")

