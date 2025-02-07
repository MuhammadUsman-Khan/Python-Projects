import random

def result(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("Its a Tie!")

    elif (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors") or (computer_choice == "scissors" and user_choice == "rock"):
        print("You Win!")

    elif (computer_choice == "paper" and user_choice == "rock") or (computer_choice == "scissors" and user_choice == "paper") or (computer_choice == "rock" and user_choice == "scissors"):
        print("You lost!")

    else:
        print("Invalid Input!")


def main():
    choices = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        computer_choice = random.choice(choices)
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        print("Computer Choice: ", computer_choice)
        result(computer_choice, user_choice)
        
        choice = input("\nDo you want to play again! (yes/no): ").lower()
        if choice == "no":
            print("Exiting the Rock, Paper, Scissors Game!")
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()