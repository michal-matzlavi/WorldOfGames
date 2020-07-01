import Utils
from os import path


# checks if the SCORES_FILE_NAME file exists if not it creates it. Writes the points in it
def add_score(points):
    if path.exists(Utils.SCORES_FILE_NAME):
        file = open(Utils.SCORES_FILE_NAME, "r")
        file_content = file.read()
        if file_content == "":
            score = 0
        else:
            try:
                score = int(file_content)
            except ValueError:
                print(Utils.ERROR_MESSAGE)
                file.close()
                exit()
        score += int(points)
        file = open(Utils.SCORES_FILE_NAME, "w")
        file.write(str(score))
        file.close
        print("Your score is: " + str(score))
    else:
        file = open(Utils.SCORES_FILE_NAME, "w")
        file.write(str(points))
        file.close()
        print("Your score is: " + str(points))
