import random

def generate_number():
    return random.randint(1,100)

def get_user_guess():
    while True:
        try:
            return int(input("Enter your guess from (1-100): "))
        except:
            print("Invalid Value. Enter your guess from (1-100)")


def check_guess(number, guess, attempts):
    if guess > number:
        print("Too high! Try again")

    elif guess < number:
        print("Too low! Try again")
    
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts")
        return True
    return False


def play_game():
    number = generate_number()
    attempts = 0
    print("Welcome to the number guessing game")
    while True:
        guess = get_user_guess()
        attempts += 1
        if check_guess(number, guess, attempts):
            break

def main():
    play_game()

if __name__ == "__main__":
    main()