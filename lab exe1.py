# 1 print the sum of number
# one = int(input("first number"))
# two = int(input("second number"))
# three = int(input("third number"))
# print ("The sum is ", one +two+ three)




#2 print area of right angle triangle
# b = float(input("Enter Breadth"))
# h = float(input("enter height"))
# a = 1/2*(b*h)
# print("the area if right angle triangle is", a)



# 3 to print equal no of apple distributed AND no.of remaning apple
# s =int(input("Total no of student "))
# k = int(input("total no of apple "))
# a = k // s
# n = a * s
# r = k-n
# print("each person gets ", a ,"Apple")
# print("remaning apple is ", r)



# 4 to print hour and minitue
# t = float(input("Enter hour in minitue "))
# d = t //1440
# c = d%3600
# m = c%60
# print(int(c), ":", m)




# 5 to print no of student how need bench
# s = int(input("enter no of student : "))
# f = s // 2
# r = f * 2
# c = s-r
# t = c + f
# if c==0:
#     print("Total no of bench required is", f)
# else:
#     print("the total no of bench required is", t)




# 6 to print BMI (Body Mass Index)
# m = int(input("enter your weight in KG "))
# h = int(input("enter height in meter "))
# b = m/(h**2)
# print("your Body Mass Index is :", b)





 # 7
# dist = 4 #miles
# speed = 25 #mph
# min = 2 #minutes
# stop = 10
#
# def bus_time():
#     time = dist / speed * 60
#     final_Time = time + stop_time()
#     return final_Time
#
# def stop_time():
#     return 2 * 10
#
# def run_time():
#     first_time =  7 * 60
#     second_and_third_time = 2/(15 * 60)
#     last_time = 7 * 60
#     return first_time + second_and_third_time + last_time
#
# print("Bus will take " + str(bus_time()) + " minutes")
# print("Jogging will take " + str(run_time()) + " minutes")






 # 8  to print area of circle
# r = int(input('enter radius'))
# pi = 3.14
# a = pi*r**2
# print('the area is', a)





# 9
# count = int(input("Enter the count for sum"))
# sumValue = 0
# def sum(n):
#     return (n * (n + 1)) / 2
#
# for i in range(count):
#     sumValue += sum(i)
#
# print(sumValue)






# 10 to print day,hr,min,sec
# n = int(input("enter second"))
# day = n//(24*3600)
# print('the day : ',day)
# n = n%(3600*24)
# hour = n//3600
# n = n%(3600)
# min = n//60
# print("the hr is : ",hour)
# print("the min is : ",min)
# n = n%60
# print("the sec is : ",n)


# ----------------------------------------------------------------------
# to print each number
# n = 345
# b = n//100
# print(b)
# c = (n-b*100)//10
# print(c)
# a = n-b*100-c*10
# print(a)



#multiple of 2up to 10 using while loop
# n =int(input("enter a number"))
# b = 1
# while b <=10:
#     print(n ,"*", b, "=", n*b)
#     b = b + 1




# to print odd or even by usinf function
# def num(a):
#     b=(a%2)
#     x = b
#     if b ==0:
#         print("even")
#     else:
#         print("odd")
#         return (x)
#
# num(4)



# TO PRINT IT IS UPPER CASE OR IN LOWERCASE
# def name(c):
#     if c.isupper():
#         a="it is uppercase"
#     else:
#         a="it is lower case"
#     return a
# z=str(input("enter name :"))
# print(name(z))


# print matrix form based on user
# A = [[1,2,3,4],[5,6,7,8]]
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i][j])









