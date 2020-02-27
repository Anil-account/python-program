# s = "hello"
# print(len(s))  to count words
# print(s.upper())  makes word in uppercase
# print(s.lower()) make words in lower case
# s_u = s.upper()
# s_l = s.lower()
# print(s.replace('h', 'H')) replace word
# ss = s.replace('h', 'H')
# print(ss)
# print(s.count('l'))  count total number of assigned words


# # string to list
# s = "Hello"
# l = list(s)
# print (l)
# l.count('h')
# a = ''.join(l)
# print(a)
# s = "words can be seperated in this way"
# x = s.split()
# print(x)
#
# b = "hello world"
# for word in s:
#     print(word)


# letter = chr(2)
# print(letter)

# for i in range(3):
#     print(i)
#     print(i+1)


# b = "Anilthapa"
# print(b.strip())
# print(0.1+0.2==0.3)
# print("hi user"[::-1])
# print(complex(2,3))
# print('{0:.2}'.format(1.0/3))
# print('{0:-2%}'.format(1.0/3))
# i = 0
# while i < 3:
#     print(i)
#     i += 1
# else:
#     print(0)
#
# print('abcefd'.replace('cd','12'))
# def f(value,values):
#     v= 1
#     values[0] = 44
# t = 3
# v = [1,2,3]
# f(t,v)
# print(t,v[0])

# l = [12,23,44,55,23,88]
# print(l[0])
# print(l[1:5])
# print(l[1:])
# print(l[:3])
# print(l[1:5:2])
# print(l[::-1])


# s = "python is cool"
# print(s[0])
# print(s[1:5])
# print(s[1:])
# print(s[:3])
# print(s[1:5:2])
# print(s[::-1])

# b = [i for i in range(1,6)]
# print(b)

# l = []
# for i in range(1,6):
#     l.append(i)
# print(l)

# l = []
# for i in range(5):
#     num = int(input("enter a num:"))
#     l.append(num)
# print(l)

# l1 = [1,2,3,4]
# l2 = []
# for num in l1:
#     l2.append(num**2)
#
# l2 = [num**2 for num in l1]
# print(l2)

# l1 = [1,2,3,4]
# l2 = []
# for num in l1:
#     if num%2==0:
#         l2.append(num)
#
# l2 = [num for num in l1 if num%2==0]
# print(l2)

#PUT 5 RANDOM IMPORT RANDINT
from random import randint
l = []
for i in range(5):
    l.append(randint(1,10))

l = [randint(1,10)]



# y= 8
# z = lambda x : x * y
# print (z(6))


# to find odd or even
# def res(a):
#     b = a%2
#     if b == 1:
#         print("it is odd")
#     else:
#         print("it is even")
#         return b
#
# a = int(input("enter a number"))
# res(a)
#
