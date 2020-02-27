# 1 to find number divisible by 5 and 7
# a = 1500
# b = 2700
#
# index = a
#
# while index <= b:
#     if index % 7 == 0 and index % 5 == 0:
#         print(index)
#     index += 1






# 2 to convert temperature
# def toCelsius(f):
#     return (5/9) * (f - 32)
#
# def toFahrenheit(c):
#     return (9/5 * c) + 32
#
#
# print(toCelsius(98))
# print(toFahrenheit(37))







# 3to guess correct num
# word = 9
#
# wrongGuess = True
#
# while  wrongGuess:
#     number = int(input("Guess a number"))
#     if number == word:
#         wrongGuess = False
#         print("Well guessed!")








# 4 to make star
# def show_star(count):
#     star = ""
#     for i in range(count + 1):
#         star += "*"
#
#     print(star)
#
# for i in range(5):
#     show_star(i)
# for j in range(i - 1, -1, -1):
#     show_star(j)








# 5 def to reverse word
#     reversedString = ""
#     index = len(string)
#     while index > 0:
#         reversedString += string[index - 1]
#         index = index - 1
#     return reversedString
#
# word = input("Enter a word")
# print(reverse(word))







# 6 to count odd or even
# num = []
# odd = 0
# even = 0
#
# for i in range(100):
#     num.append(i)
#
# for item in num:
#     if item % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#
# print(odd)
# print(even)








# 7 to print number
# num = []
# for i in range(7):
#     num.append(i)
#
# for item in num:
#     if item % 3 != 0:
#         print(item)








# 8 to get fibonacci series
# def fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(fibo(n-1) + fibo(n-2))
#
# index = 0
# while 1:
#     number = fibo(index)
#     if number > 50:
#         break
#     print(number)
#     index += 1







# 9 find factorial num
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(1))







#  10 to calculate string and numbers
# s = input("Input a string")
# d = 0
# v = 0
# for c in s:
#     if c.isdigit():
#         d = d+1
#     elif c.isalpha():
#         v = v+1
#     else:
#         pass
# print("Letters", v)
# print("Digits", d)







# LIST
# 1 To sum
# items = [8,9,5,2,1,3]
# sum = 0
# for item in items:
#     sum += item
# print(sum)






# 2 to multiply item in list
# items = [1,3,4,55,1,22]
# multiply = 1
# for item in items:
#     multiply *= item
# print(multiply)






# 3 to print max num
# items = [1,2,3,5,6,7]
# item =max(items)
# print(item)






# 4 to print smallest
# items = [23,45,67,88,99]
# item = min(items)
# print(item)






# # 6to check list's empty or not
# l = [1]
#
# if len(l) <= 0:
#     print("list empty")
# else:
#     print(" list not empty")






# 7 yo copy items
# items = [1,2,3,4,5,6]
# newItems = items.copy()
# print(newItems)








# 8 to print item after removing element
# items = [88,55,22,33,66,1,44,77]
# del(items[0])
# print(items)
# del(items[3])
# print(items)
# del(items[3])
# print(items)







# 9 to select  item randomly
# from random import randint
# items = [1,2,3,4,5,6]
# value = randint(0, len(items)-1 )
# print(items[value])





#TUPLE
# 3to print tuple
# tup = (1,2,3)
# print(tup)






# 2 to create tuple with different data types and print
# tup = ('Anil',23,98.88,-12)
# print(tup)

# print(tup[2])







# 4 to unpack tuple with several variable
# t = ('Anil','Koteshwor','27A')
#
# (name, address, batch) = t
#
# print(college)
# print(address)
# print(batch)








# 5 add item in tuple
# a = ('Anil','koteshwor','27A')
# b = a + tuple("computing")
# print(b)
#
# tup = ('Anil','Koteshwor','27A')
# dummyString = ''.join(tup)
# print(dummyString)









#  7 to get element from tuple
# tup = (1,2,3,4,5,6,7,8,9,10,11,12)
# print(tup[3])
#
# print(tup[-4])








# 8 to create clone of tuple
# from copy import deepcopy
#
# tup = ([],2,3,4,5,6,7,8,9,10,11,12)
# newTup = deepcopy(tup)
# newTup[0].append("yellow")
#
# print(newTup)








# SET
#1 to print set
# set = {'apple', 'ball', 'cat'}
# print(set)
#
# set = {'apple', 'ball', 'cat'}
# for item in set:
#     print(item)








# 2 to iterate set
# set = {1, 2, 3}
# set.add(4)
# print(set)







# 3 and 4 to add member in set ang remove
# set = {1, 2, 3}
# set.add(4)
# set.remove(2)
# print(set)







# 5 to remove item
# set = {1, 2, 3}
#
# for item in set:
#     if item == 2:
#         set.remove(item)
#         break
# print(set)







#6 to create intersection set
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
#
# intersection = set1.intersection(set2)
#
# print(intersection)









#DICTIONARY
# 1to sort dictionary
# dict =	{"1": 1, "2": 2, "3": 3}
# dict["4"] = 4
#
# print(dict)








# 3 to conccatenete
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
#
# dict4 = dict(dic1)
# dict4.update(dic2)
# dict4.update(dic3)
# print(dict4)







#4 to check dictionary if exist or not
# dict =	{"1": 1, "2": 2, "3": 3 }
#
# keys =  dict.keys()
#
# for item in keys:
#     if item == '4':
#         print("key exists")
#         break
#     else:
#         print("key doesn't exist")









#  6 to generate dictionary
# number = 5
# dictionary = dict()
# for i in range(number):
#     key = i + 1
#     dictionary.update({ str(key): key * key})
#
# print(dictionary)








# 7 to print script merge dictionary
# number = 15
# dictionary = dict()
# for i in range(number):
#     key = i + 1
#     dictionary.update({ str(key): key * key})
#
# print(dictionary)










# 9 to iterate over dictionaries
# dict1 =	{"1": 1, "2": 2, "3": 3 }
# dict2 =	{"4": 4, "5": 5, "6": 6 }
#
# dict4 = dict1
# dict4.update(dict2)
# print(dict4)








# 10 to add item in dictionary
# dict1 = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6}
# sum = 0
# values = dict1.values()
# for item in values:
#     sum += item
# print(sum)



