import random
number = random.randint(1,100)
guess=0
while guess!=number:
    guess = int(input("Guess a number:"))
    if guess<number:
        print("You loose the game! \nNumber is low")
    elif guess>number:
        print("You loose the game! \nNumber is High")
    else:
        print("Congratulations,You Won the game!")
        break
