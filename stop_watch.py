import time

def stopwatch():
    print("Stopwatch started. Press ENTER to stop.")
    start_time = time.time()
    input()
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {int(elapsed_time // 60)} min {int(elapsed_time % 60)} sec")

def countdown_timer():
    minutes = int(input("Enter countdown time in minutes: "))
    seconds = minutes * 60
    
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"Time Left: {mins} min {secs} sec", end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("Time's up! ⏰")

def main():
    while True:
        print("\n===== Stopwatch & Timer =====")
        print("1. Start Stopwatch")
        print("2. Start Countdown Timer")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            stopwatch()
        elif choice == "2":
            countdown_timer()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
