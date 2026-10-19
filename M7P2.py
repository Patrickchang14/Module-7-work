# Module 7 M7P2 Patrick Chang Oct 18, 2026

#Inputs
start = float(input("Enter start value: "))
stop = float(input("Enter stop value: "))
increment = float(input("Enter increment value: "))

#Loop
current = start

#Increments
if increment > 0:
    while current <= stop:
        print(current)
        current += increment
elif increment < 0:
    while current >= stop:
        print(current)
        current += increment
else:
    print("Increment value cannot be zero, please enter a different value.")