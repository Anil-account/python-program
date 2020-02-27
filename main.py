import operation


success = False
while success == False:
    try:

        a = int(input("enter a num "))
        b = int(input("enter a num "))
        o = input("enter a operation( /, *, -, +, ) : ")
        if o == "+":
            print("the addition is ", operation.add(a,b))
        elif  o == "-":
            print("the subttaction is ", operation.subtract(a,b))
        elif o =="*":
            print("the multiplication is ", operation.multiply(a,b))
        elif o == "/":
            print("the divide is ", operation.divide(a,b))
    except:
        print("Dummy you press the wrong key")