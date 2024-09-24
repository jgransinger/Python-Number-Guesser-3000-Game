import random
from art import logo

def calc_guess(guess):
    if guess > number and 0 < guess < 100 and attempts > 0:
        if attempts > 0:
            calc_attempts()
            guess = int(input("TOO HIGH! Guess again\n"))
            (print(f"You have {attempts} guesses left. Be careful!"))
            calc_guess(guess)
    elif guess == number:
        print("HOLY SMOKES, YOU GOT IT. YOU WIN!")
    elif guess < number and 0 < guess < 100 and attempts > 0:
        if attempts > 0:
            calc_attempts()
            guess = int(input("TOO LOW! Guess again\n"))
            (print(f"You have {attempts} guesses left. Be careful!"))
            calc_guess(guess)
    else:
        print("Stay between 1 and 100 next time. Game Over. Please restart game.")

def calc_attempts():
    global attempts
    attempts -= 1
    if attempts <= 0:
        print("You Lose! No more attempts left. Sorry my dude.")

#START OF GAME

print(logo)
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n").lower()
number = random.randint(1,100)
attempts = 0

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("Uhh. That was not it. Restart the game. ")
print(f"You have {attempts} guesses remaining. Good luck!") #shows not defined in IDE but works due to no block scope in python
print(f"The answer is: {number}") ## DELETE THIS AFTER TESTING
calc_guess(int(input("What is your first guess?: \n")))

