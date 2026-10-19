# M7P4 Module 7 Patrick Chang Oct 18, 2026

#Declare variables
total_gross_pay = 0.0
employee_count = 0

#Prompt before loop
continue_program = input("Do you want to run the program? (Type 'Yes' to run program: ")

#While loop
while continue_program == "Yes":
  last_name = input("Enter last name: ")
  hours_worked = float(input("Enter hours worked: "))
  rate_of_pay = float(input("Enter rate of pay: "))

  #If statements and calculations
  if hours_worked > 40:
    regular_pay = 40 * rate_of_pay
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (rate_of_pay * 1.5)
    gross_pay = regular_pay + overtime_pay
  else:
    gross_pay = hours_worked * rate_of_pay

  #Increments
  total_gross_pay += gross_pay
  employee_count += 1

  #Outputs
  print(f"Employee last name is: {last_name} and their Gross Pay is: ${gross_pay:.2f}")

  #Second loop prompt
  continue_program = input(
      "Would you like to process another employee? (type 'Yes' to continue or any other key to quit): "
  )

#Outputs for loop finish
print(f"Total number of employees is: {employee_count}")
print(f"Sum of all gross pays is: ${total_gross_pay:.2f}")

if employee_count > 0:
  average_pay = total_gross_pay / employee_count
  print(f"Average pay is: ${average_pay:.2f}")
else:
  print("No employee data was entered.")