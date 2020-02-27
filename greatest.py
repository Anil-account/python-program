# a = int(input("enter a number"))
# b = int(input("enter second number"))
# c = int(input("enter third number"))
# if (a > b) and (a > c):
#     temp = a
# elif (b > a) and (b > c):
#     temp = b
# else:
#     temp = c
#     print("The greatest number is ", temp)

l = [44,88,90]
l1 = ['sci','eng','mths']
def high(l):
    a = 0
    for i in range (len(l)):
        if l[i]==max(l):
            a = i

    return a
print(high(l))
print(l1[high(l)])
print(max(l))
