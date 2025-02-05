def show_menu():
    print("\n===== Flashcard App =====")
    print("1. Add Flashcard")
    print("2. View Flashcards")
    print("3. Practice Flashcards")
    print("4. Delete Flashcards")
    print("5. Exit")

def add_flashcard(flash_cards):
    while True:
        question = input("Enter the question: ").strip()
        if not question:
            print("Question cannot be empty. Try Again!")
            continue

        if question in flash_cards:
            print("Question already exists. Try another one!")
            continue

        answer = input("Enter the answer: ").strip()
        if not answer:
            print("Answer cannot be empty. Try Again!")
            continue

        flash_cards[question] = answer
        print("Flashcard added successfully!\n")

        another = input("Do you want to add another (yes/no): ").strip().lower()
        if another != "yes":
            break

    print("Exiting to main menu....\n")



def view_flashcards(flash_cards):
    if not flash_cards:
        print("No cards available!")

    else:
        print("\n===== All Flashcards =====")
        for question, answer in flash_cards.items():
            print(f"Q: {question}")
            print(f"Ans: {answer}")
            print(f"-----------------")
  
def practice_flashcards(flash_cards):
    if not flash_cards:
        print("No flashcards available for quiz!")

    else:
        print("\n===== Quiz Mode =====")
        score = 0
        for question, correct_answer in flash_cards.items():
            user_answer = input(f"Q: {question} ").strip()
            if user_answer.lower() == correct_answer.lower():
                print("Correct!")
                score += 1
            
            else:
                print(f"Incorrect! The right answer is {correct_answer}\n")

        print(f"Your final score is {score}/{len(flash_cards)}\n")


def delete_flashcard(flash_cards):
    if not flash_cards:
        print("No flashcards available to delete!")
    
    else:
        view_flashcards(flash_cards)
        question = input("Enter the exact question to delete: ").strip()

        if question in flash_cards:
            del flash_cards[question]
            print("Flashcard deleted successfully!")

        else:
            print("Question not found in Flashcards")
        

def main():
    flash_cards = {}  
    while True:
        show_menu()
        choice = input("Choose your choice: ")

        if choice == "1":
            add_flashcard(flash_cards)

        elif choice == "2":
            view_flashcards(flash_cards)

        elif choice == "3":
            practice_flashcards(flash_cards)

        elif choice == "4":
            delete_flashcard(flash_cards)

        elif choice == "5":
            print("Exiting Flashcard App. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

