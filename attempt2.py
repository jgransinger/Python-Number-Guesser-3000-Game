import random
from art import logo

def calc_guess(guess):
    if 0 < guess < 100:
        if guess > number:
            deduct_attempt(1)
            try_again = int(input("Too high. Choose a new number: "))
            print_attempts()
            new_guess(try_again)
        elif guess < number:
            deduct_attempt(1)
            try_again = int(input("Too low. Choose a new number: "))
            print_attempts()
            new_guess(try_again)
        elif guess == number:
            print("You win")
    else:
        print("Invalid number.")

def new_guess(new_num):
    calc_guess(new_num)

def choose_difficulty(diff_choice):
    attempts = 0
    if diff_choice == "easy":
        attempts = 10
        print(f"You have {attempts} attempts left")
    elif diff_choice == "hard":
        attempts = 5
        print(f"You have {attempts} attempts left")
    return attempts

def deduct_attempt(x):
    global attempts
    if attempts > 0:
        attempts -= x
    else:
        print("No more attempts. you lose.")

def print_attempts():
    print(f"you have {attempts} attempts left.")

##START OF GAME

number = random.randint(1,100)
print(f"The number is: {number}") # delete this in final version
attempts = choose_difficulty(input("Choose difficulty. Type 'easy' or 'hard': "))
calc_guess(int(input("Guess a number: ")))


