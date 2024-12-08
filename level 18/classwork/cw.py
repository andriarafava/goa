for number in range(0, 21, 2):
    print(number)

    for i in range(1, 20, 2):
    print(i)




    for i in range(10, 31):
    print(f"{i} - {'even' if i % 2 == 0 else 'odd'}")





    # მომხმარებლის მიერ შეყვანილი ორი რიცხვი
num1 = int(input("15: "))
num2 = int(input("10: "))

# შედეგების დამუშავება
if num1 > num2:
    # დიაპაზონი num2-დან num1-მდე და ლუწი რიცხვების ბეჭდვა
    numbers = [i for i in range(num2, num1 + 1) if i % 2 == 0]
else:
    # დიაპაზონი num1-დან num2-მდე და კენტი რიცხვების ბეჭდვა
    numbers = [i for i in range(num1, num2 + 1) if i % 2 != 0]

# რიცხვების ბეჭდვა
print("10,12,14:", numbers)

# ჯამი
total_sum = sum(numbers)
print("36:", total_sum)


num1 = int(input("10 (num1): "))
num2 = int(input("5(num2): "))

# შედეგების სია და ჯამი
numbers = []
total_sum = 0

# პირობები
if num1 > num2:
    numbers = [x for x in range(num2, num1 + 1) if x % 2 == 0]
else:
    numbers = [x for x in range(num1, num2 + 1) if x % 2 != 0]

# ჯამის გამოთვლა
total_sum = sum(numbers)

# შედეგების დაბეჭდვა
print("დაბეჭდილი რიცხვები:", numbers)
print("მათი ჯამი:", total_sum)