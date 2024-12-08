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
Explanation: