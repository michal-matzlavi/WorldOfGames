import random
import Score
import Live
from Utils import ERROR_MESSAGE


# returns a random number between one and difficulty
def generate_number(difficulty):
    rand_num = random.randint(1, difficulty)
    return rand_num


# returns int input from user
def get_guess_from_user(difficulty):
    guess = 0
    try:
        guess = int(input("Enter a number between 1 and " + str(difficulty) + ":"))
    except ValueError:
        print(ERROR_MESSAGE)
    return guess


# compares the random number and the guess returns a boolean
def compare_results(difficulty, secret_number):
    return generate_number(difficulty) == secret_number


# plays the guess game if the user wins it ads the points according to
# difficulty to the score file if not it loads Wog again
def play(difficulty):
    secret_number = get_guess_from_user(difficulty)

    if compare_results(difficulty, secret_number):
        print("You won!")
        Score.add_score(difficulty)
        return True
    else:
        print("You lost")
        Score.add_score(0)
        Live.load_game()
        return False
