# to fi=nd greatest
# def max(a,b,c):
#     if a > b and a > c:
#         print("maximum is :", a)
#     elif b > a and b > c:
#         print("maximum is :", b)
#     else:
#         print("maximum is :", c)
#
# numbers = max(12, 23, 44)







#  2 function to call fizz_buzz

# def fizz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0 :
#         print("Fizz")
#     else:
#         print("error num")
# number = fizz(int(input('enter number')))







#  # 3 to find odd or even

# def find(limit):
#
#     for i in range(limit):
#         if i % 2 == 0:
#             print(str(i) + " Even")
#         else:
#             print(str(i) + " Odd")
# limit = find(int(input("Enter your limit")))






#4 to print number multiple of sum of 3 and 5
#
# n = int(input("enter a num"))
# l = []
# for i in range(1,n+1):
#      a = 3*i
#      l.append(a)
#      b = 10*i
#      l.append(b)
# l.sort()
# print(l)
#






# 5 to form a star
# def star(rows):
#     s = ""
#     for i in range(rows+1):
#         s += "*"
#     print(s)
#
# for i in range(5):
#     star(i)






# 6 to print reverse of string
# def string(str):
#     rev = ""
#     for i in range(1,len(str)+1):
#         rev +=str[-i]
#     print(rev)
# str = (string("hello"))






#7 to count uppercase and lowercase
# def cou(str):
#     count = 0
#     count1 = 0
#     for i in range(len(str)):
#         for j in range(len(str[i])):
#             rev = str[i][j]
#             if rev.isupper():
#                 count += 1
#             elif rev.islower():
#                 count1 +=1
#     print('uppercase is ',count)
#     print('lowercase is ',count1)
# str = cou("HelloWorld")








# 8  to print prime or not

# def checkPrime(number):
#     index = 2
#     while (index < number):
#         if number % index == 0:
#             return False
#         index += 1
#     return True
#
# print(checkPrime(12))







# 9 to check if palindrome or not
# def reverse(string):
#     reversedString = ""
#     index = len(string)
#     while index > 0:
#         reversedString += string[index - 1]
#         index = index - 1
#     return reversedString
#
# data = ["Hello", "madam"]
# for item in data:
#     if item == reverse(item):
#         print(str(item) + " is palindrome")
#     else:
#         print(str(item) + " is not palindrome")







# 10 to display srting present at even position
# def str(input):
#     length = len(input)
#     index = 0
#     while(index < length):
#         if index % 2 == 0:
#
#             print(input[index])
#
#         index += 1
#
# input = str(input("Enter a string "))




# -----------------------------------------------------------------------------------------------------





#  to find the factorial of a number using functions
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(23))