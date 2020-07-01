import random
import Utils
import Score
import Live


# returns a list of numbers between one and difficulty
def generate_sequence(difficulty):
    sequence = []
    for x in range(difficulty):
        rand_num = random.randint(1, 101)
        sequence.append(rand_num)
    return sequence


# returns a list of numbers from the user the list'd length is difficulty
def get_list_from_user(difficulty):
    user_list = []
    user_list_num = 0
    print("After seeing the numbers enter the numbers you saw, each one separated with Enter.")
    for x in range(difficulty):
        try:
            user_list_num = int(input())
        except ValueError:
            print(Utils.ERROR_MESSAGE)
            break
        user_list.append(user_list_num)
    return user_list


# checks if two lists are equal returns a boolean
def is_list_equal(list_a, list_b):
    return list_a == list_b


# plays the memory game if the user wins it ads the points according to
# # difficulty to the score file if not it loads Wog again
def play(difficulty):
    list_a = generate_sequence(difficulty)
    print(list_a)
    Utils.screen_cleaner()
    list_b = get_list_from_user(difficulty)
    if is_list_equal(list_a, list_b):
        print("You won!")
        Score.add_score(difficulty)
        return True
    else:
        print("You lost")
        Score.add_score(0)
        Live.load_game()
        return False
