import os
from time import sleep

SCORES_FILE_NAME = "Scores.txt"
ERROR_MESSAGE = "Something went wrong..."


# clears the screen
def screen_cleaner():
    sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')

