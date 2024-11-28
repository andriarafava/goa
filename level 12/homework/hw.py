bool1 = True
bool2 = False

# ლოგიკური ოპერატორების გამოყენება
print(bool1 and bool2)  # შედეგი იქნება False, რადგან bool2 False-ია
print(bool1 or bool2)   # შედეგი იქნება True, რადგან bool1 True-ია

# სამი ბულიანური ცვლადი
bool3 = True

# ლოგიკური ოპერატორების გამოყენება
print(bool1 and bool2 and bool3)  # შედეგი იქნება False, რადგან bool2 False-ია
print(bool1 or bool2 or bool3)    # შედეგი იქნება True, რადგან bool1 True-ია


# მაგალითი 1: ბულეანური ცვლადების შედარება
a = 5
b = 10
print(a < b and b > 8)  # True, რადგან a < b და b > 8

# მაგალითი 2: ორი ბულეანის შედარება 'and' ოპერატორით
x = True
y = False
print(x and y)  # False, რადგან y არის False

# მაგალითი 3: ორი ბულეანის შედარება 'or' ოპერატორით
x = True
y = False
print(x or y)  # True, რადგან x არის True

# მაგალითი 4: მთელი რიცხვების შედარება და 'and' ოპერატორის გამოყენება
age = 25
height = 170
print(age > 18 and height > 160)  # True, რადგან ორივე პირობა შესრულებულია

# მაგალითი 5: მთელი რიცხვების შედარება და 'or' ოპერატორის გამოყენება
age = 16
height = 170
print(age > 18 or height > 160)  # True, რადგან height > 160

# მაგალითი 6: 'not' ოპერატორის გამოყენება
is_sunny = False
print(not is_sunny)  # True, რადგან is_sunny არის False

# მაგალითი 7: შედარება ორი რიცხვისთვის 'and' ოპერატორით
num1 = 8
num2 = 12
print(num1 != num2 and num1 < num2)  # True, რადგან num1 != num2 და num1 < num2

# მაგალითი 8: შედარება ორი რიცხვისთვის 'or' ოპერატორით
num1 = 8
num2 = 12
print(num1 == num2 or num1 < num2)  # True, რადგან num1 < num2

# მაგალითი 9: შედარება მთელ რიცხვებს შორის, 'not' ოპერატორი
x = 15
y = 20
print(not (x == y))  # True, რადგან x != y

# მაგალითი 10: მთელი რიცხვი, შედარება და 'and' ოპერატორი
a = 30
b = 40
c = 25
print(a < b and c < a)  # True, რადგან a < b და c < a