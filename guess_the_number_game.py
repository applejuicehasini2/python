# import necessary modules
import random
import time

# Pick a number between 1 and 100
numberToBeGuessed = random.randint(1, 100)

def checkGuess(numberToBeGuessed, guess):
    if guess < numberToBeGuessed:
        print("Your guess is too low.")
        return("low")
    elif guess > numberToBeGuessed:
        print("Your guess is too high.")
        return("high")
    else:
        print("Correct!")
        return("correct")

def playGame():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    numberToBeGuessed = random.randint(1, 100)
    guess = None
    guessCount = 0

    while guess != numberToBeGuessed:
        guess = input("Enter your guess: ")
        guess = int(guess)
        guessCount += 1

        result = checkGuess(numberToBeGuessed, guess)

        if result != "correct":
            print("Try again.")
            print("Number of guesses so far: " + str(guessCount))
        else:
            print("Congratulations! You guessed the number in " + str(guessCount) + " guesses.")
            break

    playAgain = input("Do you want to play again? (yes or no): ")
    if playAgain.lower() == "yes":
        playGame()
    else:
        print("Thanks for playing!")

def playGameWithHint():
    print("Welcome to the number guessing game with hints!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    numberToBeGuessed = random.randint(1, 100)
    guess = None
    guessCount = 0

    while guess != numberToBeGuessed:
        guess = input("Enter your guess: ")
        guess = int(guess)
        guessCount += 1

        result = checkGuess(numberToBeGuessed, guess)

        if result != "correct":
            print("Try again.")
            print("Number of guesses so far: " + str(guessCount))

            if abs(numberToBeGuessed - guess) <= 10:
                print("Hint: You're very close!")
            elif abs(numberToBeGuessed - guess) <= 20:
                print("Hint: You're close.")
            else:
                print("Hint: You're far off.")
        else:
            print("Congratulations! You guessed the number in " + str(guessCount) + " guesses.")
            break

    playAgain = input("Do you want to play again? (yes or no): ")
    if playAgain.lower() == "yes":
        playGameWithHint()
    else:
        print("Thanks for playing!")

playAgain = "yes"
while playAgain.lower() == "yes":
    gameType = input("Do you want to play 'normal' or 'hinted'?: ")
    if gameType.lower() == "normal":
        playGame()
    elif gameType.lower() == "hinted":
        playGameWithHint()
    else:
        print("Invalid input. Please enter 'normal' or 'hinted'.")
    playAgain = input("Do you want to play again?")