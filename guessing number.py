#GUESSING THE NUMBER GAME

import random
ans = random.randint(0, 101)

lives = 10
should_continue = True
while should_continue:

    user = int(input("enter the number :  "))
    
    if user == ans:
        print("Yay you guessed correct you won ")
        should_continue = False
    elif user > ans:
        lives -=  1
        print(f"The guess is greater that answer and lives {lives}")
    elif user < ans:
        lives -= 1
        print(f"the guess is lesser than the answer and lives {lives} ")
    if lives == 0:
        should_continue = False
        print("game over ")