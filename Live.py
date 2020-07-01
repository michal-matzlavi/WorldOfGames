import GuessGame
import MemoryGame
from Utils import ERROR_MESSAGE
# returns a string with welcome greeting to user name
def welcome(name):
    return "Hello " +  name  + " and welcome to the World of Games (WoG).\nHere you can find many cool games to play."
# loads game lets users choose between guess game and memory and rus the one chosen
def load_game():
    game_num = 0
    while game_num != 1 and game_num != 2:
        try:
            game_num = int(input("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n"))
        except ValueError:
            print(ERROR_MESSAGE)
    difficulty = 0
    while difficulty > 5 or difficulty < 1:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5:"))
        except ValueError:
            print(ERROR_MESSAGE)
    if game_num == 1:
        MemoryGame.play(difficulty)
    elif game_num == 2:
        GuessGame.play(difficulty)