def word_counter(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    char_no_spaces = len(text.replace(" ",""))

    return word_count, char_count, char_no_spaces


def main():
    while True:
        print("\n===== Word Counter =====")
        text = input("Enter your text or type 'exit' to quit: ")

        if text.lower() == "exit":
            print("Exiting Word Counter. Goodbye!")
            break

        word_count, char_count, char_no_spaces = word_counter(text)

        print("\nWord Count Results:")
        print(f"Words:  {word_count}")
        print(f"Characters (Including spaces):  {char_count}")
        print(f"Characters (Excluding spaces):  {char_no_spaces}")
            

if __name__ == "__main__":
    main()