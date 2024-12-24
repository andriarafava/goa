my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num1 = int(input(" num1: "))
num2 = int(input("num2: "))


if num1 > num2:
    new_list = my_list[num2:num1]
elif num2 > num1:
    new_list = my_list[num1:num2]
else:
    new_list = []


print( new_list)


numbers = [10, 20, 30, 40, 50]


first_element = numbers[0]
third_element = numbers[2]
last_element = numbers[-1]


print("First element:", first_element)
print("Third element:", third_element)
print("Last element:", last_element)

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]


every_second_word = words[::2]


print( every_second_word)



data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


num1 = int(input((num1) ))
num2 = int(input((num2)))

if num1 > num2:
    result = data[num1:num2]
elif num2 > num1:
    result = data[num2:num1]
else:

    result = []


