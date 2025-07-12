import random

#Introduction
print("Welcome to the Rock, Paper, Scissors Game.")
print("You will play against the computer. Let's begin!")

# choices list
choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter your choice (rock, paper, scissors or 'quit' to stop:) ").lower()

    if user_choice == 'quit':
        print("Thanks for playing! Goodbye!")
        break

    # Validate user choice
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors")
        continue

    #Computer's choice generation
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    #Result
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
    (user_choice == "scissors" and computer_choice == "paper") or \
    (user_choice == "paper" and computer_choice == "rock"):
        print("You Win!")
    else:
        print("Computer wins!")