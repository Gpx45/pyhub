import time

def main():
    file = open("project1.txt", "r")
    file.read()
    file.close()

    print("\t\tWelcome to a fun and simple quiz game!!\n")
    print()
    
    name = input("What is your name? ")
    print()
    username = (name[0] + "ay" + "2")
    time.sleep(1)
    print("Your name for this game will be" ,username)

    print()


    begin = input("Do you want to play a game? (Y/N): ")
    if begin == "Y" or begin == "y":
        print("\t\t\tLet the games begin...")
        time.sleep(1)
    else:
        print("Dont be a stranger now >.<!")
        exit()
    
    print("\n------------------------------------------------------------\n")

    score = 0

    print("Who was the first person to ever send a car to space?\na. Elon Musk\nb. Jeff Bezos\nc. Bill Gates\nd. Bill Smith")
    print()
    answer = input("What is your answer? ")

    if answer == "a" or answer == "A":
        print("Correct!")
        score = score + 1
        
    else:
        print("Sorry that is incorrect, you will not earn a point!")
        score = score 
        print()

    print()

    print("\n------------------------------------------------------------\n")

    print("Where is Silicon Valley located?\na. Miami, FL\nb. San Francisco, CA\nc. Seattle, WA\nd. Denver, CO")
    print()
    answer = input("What is your answer? ")
    
    if answer == "b" or answer == "B":
        print("Correct!")
        score = score + 1
        
    else:
        print("Sorry your answer is not correct :( you will not earn a point!")
        score = score
        print()

    print(score)

    print("\n------------------------------------------------------------\n")

    print("Who owns the biggest technology company in America?\na. Samsung\nb. Snapchat\nc. Sony\nd. Apple")
    print()
    answer = input("What is your answer? ")
    
    if answer == "d" or answer == "D":
        print("Correct!")
        score = score + 1
        
    else:
        print("Sorry you have don't get any points, you will not earn a point!!") 
        print()

    print(score)

    print("\n------------------------------------------------------------\n")
    
    print("Where is Amazon's Current Headquarters?\na. Seattle, WA\nb. Boston, MA\nc. Doral, FL\nd. Ontario, Canada")
    print()
    answer = input("What is your answer? ")
    
    if answer == "a" or answer == "A":
        print("Correct!")
        score = score + 1
        
    else:
        print("Sorry your answer is incorrect!")

        
    print()

    print("Your final score is" , score)
    print()

    if score >=4:
        print("Congratulations, you got all the answers correct! Well done! :) ")
        print()

    else:
        print("Better luck next time!")

        filename = open("highscore.txt" , "w")
        
        filename.write =("\t\tCongrats on finishing the quiz!\n")
        filename.write =("Here is your final score!", score)
        filename.write = ("Next time it will be more difficult! Come back sometime!")

        filename.close()

        filename = open("highscore.txt" , "r")
        print(filename.read())
        filename.close()
        

        
        
main()

    
