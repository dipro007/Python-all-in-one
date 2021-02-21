from random import randint

for x in range(1, 6):
    guessNumber = int(input("Enter number 1 to 5 : "))
    randomNumber = randint(1, 5)

    if guessNumber == randomNumber:
        print("You have WON!")
    else:
        print("You have LOST! Try again!!")


