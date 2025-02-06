import random

def choose_word():
    words = ["apple", "banana", "guava", "grapes", "mango", "berry"]
    return random.choice(words) 


def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def main():
    word = choose_word()
    guess_letters = set()
    attempts = 6

    print("\n===== Word Guessing Game =====")
    while attempts > 0:
        print("\nWord", display_word(word, guess_letters))
        print(f"Attempts left: {attempts}")

        guess = input("Enter a letter: ").lower()

        if guess in guess_letters:
            print("You already guessed that letter!")
            continue

        guess_letters.add(guess)

        if guess in word:
            print("Correct!")
            if all(letter in guess_letters for letter in word):
                print(f"\nYou guessed the word {word}")
                print("You Win!")
                break

        else:
            print("Wrong guess!")
            attempts -= 1
        
        if attempts == 0:
            print(f"\nYou Lost! The word was {word}")


if __name__ == "__main__":
    main()

    
