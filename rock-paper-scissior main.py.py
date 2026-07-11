import random

options = ["rock", "paper", "scissors"]

while True:
    user = input("Enter rock, paper, or scissors: ").lower()

    if user not in options:
        print("Invalid choice! Please try again.")
        continue

    computer = random.choice(options)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("Match Draw!")

    elif user == "rock":
        if computer == "scissors":
            print("You Win!")
        else:
            print("Computer Wins!")

    elif user == "paper":
        if computer == "rock":
            print("You Win!")
        else:
            print("Computer Wins!")

    elif user == "scissors":
        if computer == "paper":
            print("You Win!")
        else:
            print("Computer Wins!")

    again = input("Play again? (yes/no): ").lower()

    if again != "yes":
        print("Game Over!")
        break