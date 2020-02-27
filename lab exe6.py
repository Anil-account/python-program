# 1 to find sum using recursion
# def sum(piece):
#     if len(piece) == 0:
#         return 0
#     else:
#         return piece[0] + sum(piece[1:])
#
# print(sum([1, 3, 4, 2, 5]))








# 2 to display the multiplication of 3 uoto n
# def mul(number):
#     if number == 1:
#         return 3
#     else:
#         return 3 + mul(number - 1)
#
#
# print(mul(10))







# 3 to return sum of first n intiger
# def sum(n):
#     if n <= 1:
#         return n
#     return n + sum(n - 1)
#
#
# n = 5
# print(sum(n))








# 4 to check if string is palindrome or not

# def isPalRec(st, s, e):
#     if (s == e):
#         return True
#
#     if (st[s] !=st [e]):
#         return False
#
#
#     if (s < e + 1):
#         return isPalRec(st, s + 1, e - 1)
#
#     return True
#







# 5 to check if the number is palindrome or not
# def isPalindrome(st):
#     n = len(st)
#
#     if (n == 0):
#         return True
#
#     return isPalRec(st, 0, n - 1)
#
# st = "madam"
# if isPalindrome(st):
#     print("The given string is palindrome")
# else :
#     print("The given string is not palandrome")







# 6  to check if number is palindrome or not
#
# def isPalRec(st, s, e):
#     if s == e:
#         return True
#
#     if st[s] != st[e]:
#         return False
#
#
#     if s < e + 1:
#         return isPalRec(st, s + 1, e - 1)
#
#     return True
#
#
# def isPalindrome(st):
#     n = len(st)
#
#     if n == 0:
#         return True
#
#     return isPalRec(st, 0, n - 1)
# num = int(input("enter a number"))
# if isPalindrome(str(num)):
#     print("The number is palindrome")
# else:
#     print("The number is palindrome")
