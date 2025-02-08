def show_menu():
    print("\n===== Morse Code Translator =====")
    print("1. Convert Text to Morse Code")
    print("2. Convert Morse Code to Text")
    print("3. Exit")

def text_to_code(morse_code):
    result = []
    user_input = input("Enter text to convert: ").upper()

    for char in user_input:
        if char in morse_code:
            result.append(morse_code[char])

    morse_result = ' '.join(result)

    print(f"Morse Code: {morse_result}")
    
    

def code_to_text(reverse_morse_code):
    result = []
    user_input = input("Enter Morse Code to decode: ")
    splitted_input = user_input.split()

    for code in splitted_input:
        if code in reverse_morse_code:
            result.append(reverse_morse_code[code])

    text_result = ''.join(result)

    print(f"Decoded Text: {text_result}")


def main():
    morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.','F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---','K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---','P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-','U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--','Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-','5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.','0': '-----', ' ': '/'}

    reverse_morse_code = {}

    for key, value in morse_code.items():
        reverse_morse_code[value] = key


    show_menu()
    while True:
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            text_to_code(morse_code)
        
        elif choice == 2:
            code_to_text(reverse_morse_code)

        elif choice == 3:
            print("Exiting the Morse Code Translator. GoodBye!")
            break

        else:
            print("Invalid Choice! Please try Again.")

    
if __name__ == "__main__":
    main()