
import random
random_number= random.randint(1,100)
#print(random_number)
guess_num=0
guess= None

while(guess!=random_number):
    guess= int(input("Enter Your Guess: "))
    guess_num+=1
    if(guess== random_number):
        print("You Guessed the right Number, ")
    else:
        if(guess>random_number):
            print("You Guessed The Wrong Numer,Enter A Smaller Number")
        else:
            print("You Guessed The Wrong Number,Enter A LArger Number")

print("You have Guessed The NUmber in",guess_num,"Steps.")

with open ('hiscore.txt','r') as f:
    hiscore = int(f.read())
if(guess_num<int('hiscore')):
    print("You Have Broken The High Score!")
    with open('hiscore.txt','w') as f:
        f.write(str(guess_num))



