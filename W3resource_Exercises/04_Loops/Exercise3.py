import random

def GuessNumber():
    n = int(input("Enter guess number, please. "))
    while n > 0:
        if n == random.randint(1,9):
            print("Well guessed")
            break
        else:
            print("You guess wrong! please guess again")
            n = int(input("Enter guess number, please. "))
        
      
# Main
GuessNumber()

# Way two
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')
        