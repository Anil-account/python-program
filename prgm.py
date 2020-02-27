secret_word = "Anil"
count = 0
correct = False
while count <= 3 and not correct:
    word = (input("Enter a word "))
    if word == secret_word:
        correct = True
        count += 1
        break
if correct == True :
    print("you are lucky")
else:
    print("you are not genius")
