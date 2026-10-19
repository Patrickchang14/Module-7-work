# M7P3 Module 7 Patrick Chang Oct 18, 2026

#Counter
student_count = 0

#prompt user to run the program
user_choice = input("Do you want to run this program? (Enter 'Yes' to continue): ")

#Loop
while user_choice == "Yes":
    last_name = input("Enter student's last name: ")
    score1 = float(input("Enter first exam score: "))
    score2 = float(input("Enter second exam score: "))

    #calculations
    average_score = (score1 + score2) / 2

    #Outputs
    print(f"Student's last name is: {last_name} and their average Score is: {average_score:.2f}")

    #Increments
    student_count += 1

    # Prompt user to continue the loop
    print("-" * 40)
    user_choice = input("Would you like to enter data for another student? (Enter 'Yes' to continue): ")

# This code runs after the loop ends
print("=" * 40)
print(f"The program has ended. Total number of students entered: {student_count}")
print("=" * 40)