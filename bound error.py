# a = [1,2,3]
# l = len(a)
# b = int(input("gia
# ve me num"))
# if b>= l:
#     print("invalid")

a = [1,2,3]
b = [1,4,0]
try:
    for i in range(len(a)):
        print(a[i]/b[i])
except(IndexError,ZeroDivisionError,IndentationError):
    print("there is an error in code")
