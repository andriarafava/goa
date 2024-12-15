
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


try:
    score = int(input("Enter the score (0-100): "))
    grade = determine_grade(score)
    print(f"The grade is: {grade}")
except ValueError:
    print("Please enter a valid integer score.")


def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"


try:
    number = float(input("Enter a number: "))
    result = check_number(number)
    print(f"The number is: {result}")
except ValueError:
    print("Please enter a valid number.")


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


try:
    score = int(input("Enter the score (0-100): "))
    grade = determine_grade(score)
    print(f"The grade is: {grade}")
except ValueError:
    print("Please enter a valid integer score.")


def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

try:
    number = float(input("Enter a number: "))
    result = check_number(number)
    print(f"The number is: {result}")
except ValueError:
    print("Please enter a valid number.")


def calculate_sum(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total


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
