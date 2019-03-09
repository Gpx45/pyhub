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
        answers = []
        idx = 0
        for index in ls[0:4]:
            print(index)
            answer = input("Your answer? ")
            answers.append(answer)
            if answers[idx] == checked[idx]:
                print('You are correct +1')
                score += 1
            else:
                print('You are wrong +0')
            idx += 1
            print("\n------------------------------------------------------------")
        if ls[4]:
            print("Your score is ", score)



def name_generator(name):
    """Generate the username and returns a string."""
    global username
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
    sleep(1)
    name = input("What is your name? ")
    username = name_generator(name)
    sleep(1)
    print("Your name for this game will be ",username, "\n")

    begin = input("Do you want to play a game? (Y/N): ")
    if begin == "Y" or begin == "y":
        print("\t\t\tLet the games begin...")
        sleep(1)
    else:
        print("Dont be a stranger now >.<!")
        exit()
    questions()


game()
