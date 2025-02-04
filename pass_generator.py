import random
import string


def password_genertor(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters == "y":
        characters += string.ascii_letters

    if use_numbers == "y":
        characters += string.digits

    if use_symbols == "y":
        characters += string.punctuation

    if not characters:
        return "Error! No character type selected"
    
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length for your password: "))
    use_letters = input("Include letters? (Y/N): ").lower()
    use_numbers = input("Include numbers? (Y/N): ").lower()
    use_symbols = input("Include symbols? (Y/N): ").lower()
    
    password = password_genertor(length, use_letters, use_numbers, use_symbols)
    print(f"Generated Password {password}")

if __name__ == "__main__":
    main()