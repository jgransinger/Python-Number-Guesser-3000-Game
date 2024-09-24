import random
from art import logo

def calc_guess(turns, guess):
    turns -= 1
    if 0 < guess < 100:
        if guess > number:
            print("TOO HIGH. ")
            if turns_check(turns) > 0:
                print(f"You have {turns} turns left.")
                try_again = int(input("Choose a new number: "))
                calc_guess(turns,try_again)
            else:
                print(f"The number was {number}.")
        elif guess < number:
            print("TOO LOW.")
            if turns_check(turns) > 0:
                print(f"You have {turns} turns left.")
                try_again = int(input("Choose a new number: "))
                calc_guess(turns,try_again)
            else:
                print(f"The number was {number}.")
        elif guess == number:
            print("********* YOU WIN ***********")
    else:
        print("Invalid number.")

def diff_level(choice):
    if choice == 'hard':
        attempts = 5
        print("You have 5 attempts. Good luck.")
        return attempts
    elif choice =='easy':
        print("You have 10 attempts. Good luck.")
        attempts = 10
        return attempts
    else:
        print("Invalid option. Please restart game.")

def turns_check(turns):
    if turns > 0:
        return turns
    else:
        print("No turns left. you lose!")
        return 0
##START OF GAME
print(logo)
number = random.randint(1,100)
calc_guess(diff_level(input("Choose difficulty. Type 'easy' or 'hard': ").lower()), int(input("Guess a number: ")))


