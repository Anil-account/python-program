# 1 to find 5 present or not
# l =[1,2,3,4,5]
# for i in range (len(l)):
#     if 5==l[1]:
#         print("true")
#     else:
#         print("false")





# 2 to print marks result
# mark1 = int(input("Enter your math mark :"))
# mark2 = int(input("Enter your science mark :"))
# mark3 = int(input("Enter your english mark :"))
# mark4 = int(input("Enter your nepali mark :"))
# total = mark1+mark2+mark3+mark4
# print("your total mark is ",total)
# percentage = (total/400)*100
# print("your perecentage is ",percentage)
# if percentage>70:
#     print("you got distinction")
# elif percentage>60:
#     print("you got first division")
# elif percentage>40:
#     print("you are pass")
# else:
#     print(("study hard"))
#
# print("GPA = ",percentage/25)







#  3  to print odd or even
# n = int(input("enter a limit num : "))
# for i in range(n):
#     if i%2==0:
#         print(i, "EVEN")
#     else:
#         print(i, "ODD")





# 4 to print smallest one
# i = 0
# l=[]
# while i<3:
#     a = int(input("enter a number"))
#     i = i+1
#     l.append(a)
# if l[0]<l[1] and l[0]<l[2]:
#     print(l[0], "is smallest")
# elif l[1]<l[0] and l[1]<l[2]:
#     print(l[1], "is smallest")
# elif l[2]<l[1] and l[2]<l[0]:
#
#     print(l[2], "is smallest")






# 5 to print true and false for intiger
# a = int(input("Enter a number"))
#
# if a > 0:
#     print("True")
# elif a < 0:
#     print("False")
# else:
#     print("zero")







# 6 to print intiger last digit
# n = int(input('enter three number'))
# if n<=999:
#     a = n//100
#     b = (n-(a*100))//10
#     c = (n-((a*100)+(b*10)))
#     # print(a)
#     # print(b)
#     print(c)
# else:
#     print("Invalid")






#  7 to print positive number and its fractional part
# num = float(input("enter number"))
#
# integralPart = int(num)
# fractionalPart = num - integralPart
# print("positive part is ", integralPart
# print("fraction part is ", fractionalPart)





# 8 to add sum of number
# num = int(input('enter a number'))
# def sum_digits(n):
#     s = 0
#     while n:
#         s += n % 10
#         n //= 10
#     return s
#
# print("sum of digit is", sum_digits(num))





 #  9 to find leap year or not
# year = 2001
# if (year % 4) == 0:
#     if (year % 400) == 0:
#         print(str(year) +" is a leap year")
#     else:
#         print(str(year) +" is not a leap year")
#
# else:
#     print(str(year) + " is not a leap year")






 #  10 if value are equal sum will be zero
# a = int(input("enter a number : "))
# b = int(input("enter a number : "))
# c = int(input("enter a number : "))
# if a==b or a==c:
#     print("sum is equal to '0'")
# elif b==a or b==c:
#     print("sum is zero")
# elif c==a or c==b:
#     print("sum is zero")
# else:
#     print("sum is", a+b+c)

 # 11 to find square root
 # number = 10
 # print(number**3)








 # 12 to find x
# x = 5
# x += 3
# print(x)





# 13 to print apple
# to print apple > apple
# print('Apple' > 'apple')






#  #  14 to print float
# print(float(1))








# 15 to find output of a,b,c,d
# a =int(input("enter value for a :"))
# b =int(input("enter value for b :"))
# c = int(input("enter value for c :"))
# d =int(input("enter value for d :"))
# if a == b:
#     print("a and b are equal")
# else:
#     print("a and b are not equal")
# if a != d:
#     print("a and d is not equal")
# else:
#     print("a and d is equal")
# if b == d:
#     print("b and d are equal")
# else:
#     print("b and d are not equal")
# if a != c:
#     print("a is not equal to c")
# else:
#     print("a is equal to c")
# if b > a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")
# if a < d:
#     print("d is greater than a")
# else:
#     print("d is not greater than a")
# if b-a == c-b:
#     print("b-a==c-b")
# else:
#     print("b-a==c-b is not equal")
# if b >= d:
#     print("b is greater or equal to d")
# else:
#     print("b is not greater nor equal to d")
# a += c
# print("a+c =", a)
# b /= d
# print("b/d=", d)




# ---------------------------------------------------------------------------------------------------------------------



# print individual number.
# a=("Anil")
# b = a.replace('',' ')
# print(b)
#
# for i in range(len(b)):
#     print(b[i])



 # to print factorial part
# n = int(input("enter a number"))
# a = 1
# for i in range (1,n+1):
#     a = a*i
#     print(a)

