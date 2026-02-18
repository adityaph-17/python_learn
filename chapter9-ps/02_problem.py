# The game() function in a program lets a user play a game and returns the scoreas an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random

def game():

    print("you are playing a game....")
    score = random.randint(1, 50)

    # fetch the highscore 

    with open ("txt_files/02_demo.txt", "r") as f:
        highscore = f.read()

        if (highscore != ""):
            highscore = int(highscore)

        else:
            highscore = 0

    print( f" your score is : {score}")

    if (score > highscore):

        with open ("txt_files/02_demo.txt", "w") as f:
            f.write(str(score))

    return score

game()



