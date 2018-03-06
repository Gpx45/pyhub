#!/usr/bin/python3

"""This is a quiz game."""
from time import sleep
from random import randint


def questions():
    """Split questions and assigns them toa list for display."""

    with open('quiz.txt', 'r') as stream:
        question = stream.read().split('-')
        ls = list(question)
        check = ls[4]
        checked = check.strip('\n').split(",")
        score = 0

        print(ls[0])
        answer = input("Your answer? ")
        if checked[0] == answer:
            print("You are correct! +1")
            score += 1
        else:
            print("You are wrong! +0")
        print("\n------------------------------------------------------------")
        sleep(1)

        print(ls[1])
        answer = input("Your answer? ")
        if checked[1] == answer:
            print("You are correct! +1")
            score += 1
        else:
            print("You are wrong! +0")
        print("\n------------------------------------------------------------")
        sleep(1)

        print(ls[2])
        answer = input("Your answer? ")
        if checked[2] == answer:
            print("You are correct! +1")
            score += 1
        else:
            print("You are wrong! +0")
        print("\n------------------------------------------------------------")
        sleep(1)

        print(ls[3])
        answer = input("Your answer? ")
        if checked[3] == answer:
            print("You are correct! +1")
            score += 1
        else:
            print("You are wrong! +0")
        print("\n------------------------------------------------------------")
        sleep(1)

        if score == 4:
            print("You got a perfect score of 4!!!")
        elif score == 3:
            print("you missed a perfect score of 4 by only 1 point!!!")
        elif score == 2:
            print("You missed a perfect score of 4 by only 2 points!!!")
        elif score == 1:
            print("You missed a perfect score of 4 by only 3 points!!!")
        elif score == 1:
            print("You missed a perfect score of 4 by only 4 points!!!")

        with open('highscore.txt', 'a') as stream:
            print(username, score, file=stream)


def name_generator(name):
    """Generate the username and returns a string."""
    latin = list(name)
    fletter = latin.pop(0)
    latin.append(fletter.lower())
    ay = ['a', 'y']
    latin.extend(ay)
    num = randint(0, 999)
    new_num = str(num)
    latin.append(new_num)
    new_user = ''.join(latin)
    return new_user


def game():
        """Start the quiz game."""
        print("\t\tWelcome to a fun and simple quiz game!!\n")
        print()
        sleep(1)
        name = input("What is your name? ")
        global username
        username = name_generator(name)
        sleep(1)
        print("Your name for this game will be ",username, "\n")

        begin = input("Do you want to play a game? (Y/N): ")
        if begin == "Y" or begin == "y":
            print("\t\t\tLet the games begin...")
            sleep(1)
        else:
            print("Dont be a stranger now", username, ">.<!")
            exit()

        questions()

game()
