import random
import time

def get_sentence():
    sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Practice makes a man perfect.",
    "Your time is limited, so don't waste it living someone else's life.",
    "A journey of a thousand miles begins with a single step."
    ]

    return random.choice(sentences)
    

def main():
    sentence = get_sentence()
    print("\n====== Typing Speed Checker ======")
    print(f"{sentence}\n")

    input("Press Enter to start....")
    start_time = time.time()

    user_input = input("\nStart Typing: ")

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)

    correct_chars = 0

    for original, typed in zip(sentence, user_input):
        if original == typed:
            correct_chars += 1
    if sentence:
        accuracy = (correct_chars / len(sentence)) * 100  

    else:
        accuracy = 0

    word_count = len(sentence.split())
    if time_taken > 1:
        wpm = round((word_count / time_taken) * 60, 2)

    else:
        wpm = 0

    print("\nResults:") 
    print(f"Time Taken: {time_taken} seconds")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Typing Speed: {wpm} WPM")


if __name__ == "__main__":
    main()
