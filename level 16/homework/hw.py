# Initialize the counter
count = 1

# While loop to count from 1 to 10
while count <= 10:
    print(count)  # Print the current value of count
    count += 1    # Increment the counter by 1

    # Initialize the counter
num = 2

# While loop to print even numbers between 1 and 20
while num <= 20:
    print(num)  # Print the current even number
    num += 2    # Increment by 2 to get the next even number
    # Initialize the counter
count = 10

# While loop for countdown
while count > 0:
    print(count)  # Print the current number in the countdown
    count -= 1    # Decrement the counter by 1

# Print "Blast off!" when countdown finishes
print("Blast off!")
# Define the correct password
correct_password = "mysecretpassword"

# Prompt the user for the password and keep asking until it's correct
user_password = input("Enter the password: ")

while user_password != correct_password:
    print("Incorrect password. Please try again.")
    user_password = input("Enter the password: ")

print("Access granted!")
# Define the correct username and password
correct_username = "user123"
correct_password = "mypassword"

# Initialize user inputs
username = input("Enter your username: ")
password = input("Enter your password: ")

# Keep asking for username and password until both are correct
while username != correct_username or password != correct_password:
    print("Incorrect username or password. Please try again.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

print("Login successful! Access granted.")
# Prompt the user for a number
num = int(input("Enter a number to calculate its factorial: "))

# Initialize the factorial result to 1
factorial = 1

# Use a while loop to calculate the factorial
while num > 0:
    factorial *= num  # Multiply the current factorial by num
    num -= 1  # Decrease num by 1

# Print the result
print("The factorial is:", factorial)
