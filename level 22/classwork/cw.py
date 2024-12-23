my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


user_input = int(input("50 "))


list_length = len(my_list)


if 0 <= user_input < list_length:
    print(my_list[user_input])


elif -list_length <= user_input <= -1:
    print(my_list[user_input])


