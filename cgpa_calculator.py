def get_grade_point(percentage):
    if percentage >= 85:
        return 4.0

    elif percentage >= 80:
        return 3.7

    elif percentage >= 75:
        return 3.3

    elif percentage >= 70:
        return 3.0

    elif percentage >= 65:
        return 2.7

    elif percentage >= 60:
        return 2.3

    elif percentage >= 55:
        return 2.0

    elif percentage >= 50:
        return 1.7

    else:
        return 0.0

def calculate_cgpa():
    total_point = 0
    total_credit = 0
    
    num_subjects = int(input("Enter the number of courses or subjects: "))

    for i in range(num_subjects):
        while True:

            obtained_marks = float(input(f"\nEnter obtained marks of the subject {i+1}: "))
            total_marks = float(input(f"Enter total marks of the subject {i+1}: "))
            if 0 <= obtained_marks <= total_marks:
                break
            else:
                print("Invalid input! Obtained marks should be between 0 and total marks.")

        credit_hours = int(input(f"Enter credit hours of the subject {i+1}: "))
        percentage = (obtained_marks / total_marks) * 100
        grade_points = get_grade_point(percentage)
        total_point += grade_points * credit_hours
        total_credit += credit_hours

    if total_credit == 0:
        print("No Subjects Entered!")

    else:
        cgpa = total_point / total_credit
        print(f"\nYour Cgpa is {cgpa:.2f}")

def main():
    calculate_cgpa()

if __name__ == "__main__":
    main()