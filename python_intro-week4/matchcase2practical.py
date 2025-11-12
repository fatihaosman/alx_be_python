import random

while True:
    randomNumber = random.randint(1, 5)
    guess = int(input("Guess a random number between 1 and 5: "))

    match guess:
        case _ if guess == randomNumber:
            print("🎉 Congratulations, you guessed it!")
        case _ if guess > randomNumber:
            print("Oops, your guess is a bit high. Try again!")
        case _ if guess < randomNumber:
            print("Nope, your guess is a bit low. Give it another shot!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break
