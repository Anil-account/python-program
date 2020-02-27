# def mtx(a,b):
#     A=[]
#     B=[]
#     for i in range(a):
#
#         for j in range(b):
#             B.append(1)
#         A.append(B)
#         B=[]
#
#     return A
# a=int(input('Enter no. of rows:'))
# b=int(input('Enter no. of columns:'))
# print((mtx(a,b)))




# to print 3*3 matrix
# a =[]
#
#
# for i in range(3):
#     a.append([])
#     for j in range(3):
#         a[i].append(1)
# print(a)


# to print highest marks
# result = [['name','math','eng','phy','com','nep'],
#           ['john',88.0,86.0,76.0,66.0,76.0],
#           ['sam',77.0,67.0,87.0,67.0,56.0]]
# print(result[1])
# sum = 0
# avg = 0
# for i in range(1,len(result[1])):
#     sum = result[1][i]+sum
#     avg = sum/len(result[1])-1
# print(sum)
# print(avg)
#
# print(result[2])
# for i in range(1,len(result[2])):
#     sum = result[2][i] + sum
#     avg = sum / len(result[2]) - 1
# print(sum)
# print(avg)


# find SUM OF ALL odd no of a range provided by user,
# def O(a):
#     b = 0
#     for i in range (a+1):
#         if i%2!=0:
#             b = b+i
#             print(b)
#     return(b)
#
# a = int(input("enter a number"))
# print(O(a))


A = [[1,2,3],[5,6,6]]
for i in range(len(A)):
    for j in range(len(A[1])):
        print(A[i][j])