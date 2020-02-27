# to read file
# file = open("doc.txt","r")
# print(file.read())
# file.close()

# to read file line by line
# file = open("doc.txt","r")
# lines = file.readlines()
# print(lines)
# file.close()

# file = open("doc.txt","r")
# lines = file.readlines()
# for line in lines:
#     print(line)
#     file.close()

file = open("doc1.txt","w")
for i in range(3):
     file.write(str(i))

file.close()


# file = open("doc1.txt","w")
#
# for i in range(3):
#     file.write(str(i))
#     file.write("\n")
# file.close()
