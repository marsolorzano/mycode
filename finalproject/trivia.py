#!/usr/bin/env python3

import requests
import random
from pyinputplus import inputMenu
from os import system, name
from time import sleep
# define our clear function
def screen_clear():
	if name == 'nt':
		_ = system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

def main():
    answer=input('Are you ready to play the Book Trivia Challenge? (yes/no) :')
    if answer=='yes':
        print("Let's Begin!")

    elif answer=='no':
        print("See you later then! Bye!")
        print(quit())
#    question = input("How many questions would you like to answer?(1-10):")
 #   difficulty= input("Select a difficult: (Easy, Medium, Hard, or Any)")
  #  cat= input("Choose a category: Books, Sports, Art, or Music")

# data will be a python dictionary rendered from your API link's JSON!
    URL= "https://opentdb.com/api.php?amount=10&category=10&type=multiple"
    data= requests.get(URL).json()
    score = 0
    for questiondict in data["results"]:
        print("The question is:",questiondict["question"])
        answers=questiondict["incorrect_answers"].copy()
        answers.append(questiondict["correct_answer"])
        random.shuffle(answers)
        result = inputMenu(answers, lettered=True, numbered=False)
        if result ==questiondict["correct_answer"]:
            print("Correct!")
            score += 10
            sleep(3)
            print("Next question...")
            screen_clear()
        else:
            print("Incorrect!")
            sleep(3)
            print("Next question...")
            screen_clear()
    if score >=70:
        print("Congrats! You really know your books!")
        print("Your score is:",score)
    else: 
        print("You really need to work on your book knowledge....try getting a library card!")
        print("Your score is:",score)
if __name__ == "__main__":
    main()

