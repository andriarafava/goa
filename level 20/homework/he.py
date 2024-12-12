# Function to determine grade based on score
def determine_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Invalid score'

# Input: score from the user
try:
    score = int(input("Enter the score (0-100): "))
    grade = determine_grade(score)
    print(f"The grade is: {grade}")
except ValueError:
    print("Please enter a valid integer score.")

    # Function to check if a number is positive, negative, or zero
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Input: number from the user
try:
    number = float(input("Enter a number: "))
    result = check_number(number)
    print(f"The number is: {result}")
except ValueError:
    print("Please enter a valid number.")

    # Function to determine grade based on score
def determine_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Invalid score'

# Input: score from the user
try:
    score = int(input("Enter the score (0-100): "))
    grade = determine_grade(score)
    print(f"The grade is: {grade}")
except ValueError:
    print("Please enter a valid integer score.")

# Function to check if a number is positive, negative, or zero
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
# Input: number from the user
try:
    number = float(input("Enter a number: "))
    result = check_number(number)
    print(f"The number is: {result}")
except ValueError:
    print("Please enter a valid number.")

# Function to calculate the sum of numbers between two integers
def calculate_sum(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

# Input: two integers from the user
try:
    start = int(input("Enter the start integer: "))
    end = int(input("Enter the end integer: "))
    if start > end:
        print("The start integer must be less than or equal to the end integer.")
    else:
        sum_result = calculate_sum(start, end)
        print(f"The sum of numbers between {start} and {end} is: {sum_result}")
except ValueError:
    print("Please enter valid integers.")
