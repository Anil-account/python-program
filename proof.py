guess =""
fav_word="Anil"
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != fav_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("enter a word ")
        guess_count +=1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("'you are unlucky")
else:
    print("Access Granted")
