num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

# უდიდესი რიცხვის განსაზღვრა
if num1 > num2:
    print(f"უდიდესი რიცხვი არის: {num1}")
elif num1 < num2:
    print(f"უდიდესი რიცხვი არის: {num2}")
else:
    print("ორივე რიცხვი თანაბარია.")


    number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")


    correct_password = "Goa best"

# Counter for incorrect attempts
incorrect_attempts = 0

while True:
    # Prompt the user to enter a password
    entered_password = input("Enter the password: ")
    
    # Check if the entered password is correct
    if entered_password == correct_password:
        print("Access granted!")
        break
    else:
        incorrect_attempts += 1
        print("Incorrect password. Try again.")

# Display the count of incorrect attempts
print(f"Total incorrect attempts: {incorrect_attempts}")



number = float(input("Enter a number: "))

# Check the number's status
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


    # მომხმარებლის მიერ რიცხვის შეყვანა
number = int(input("შეიყვანეთ რიცხვი: "))

# შემოწმება თუ რიცხვი 5-ზე უნაშთოდ იყოფა
if number % 5 == 0:
    print("რიცხვი 5-ზე უნაშთოდ იყოფა.")
else:
    print("რიცხვი 5-ზე უნაშთოდ არ იყოფა.")

    # Correct password
correct_password = "Goa best"

# Counter for incorrect attempts
incorrect_attempts = 0

# Loop to prompt user until the correct password is entered
while True:
    # Ask the user to enter the password
    password = input("Enter the password: ")
    
    # Check if the entered password is correct
    if password == correct_password:
        print("Correct password! Access granted.")
        break
    else:
        # Increment incorrect attempts and notify the user
        incorrect_attempts += 1
        print("Incorrect password. Try again.")

# Print the total number of incorrect attempts
print(f"Number of incorrect attempts: {incorrect_attempts}")



def calculator():
    print("Welcome to the Simple Calculator!")
    try:
        # Input the first number
        num1 = float(input("Enter the first number: "))
        
        # Input the operator
        operator = input("Enter an operator (+, -, *, /): ")
        
        # Input the second number
        num2 = float(input("Enter the second number: "))
        
        # Perform the calculation based on the operator
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:  # Check for division by zero
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return
        else:
            print("Error: Invalid operator.")
            return
        
        # Display the result
        print(f"The result of {num1} {operator} {num2} is: {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers.")
    
    print("Thank you for using the Simple Calculator!")
