# მომხმარებლისგან რიცხვის შემოტანა
number = int(input("შეიყვანეთ მთელი რიცხვი: "))

# ჯამის დასანგარიშებლად ცვლადის ინიციალიზაცია
total_sum = 0

# for ციკლი დიაპაზონის გასავლელად
for i in range(0, number + 1):  # დიაპაზონი 0-დან შეყვანილ რიცხვამდე
    total_sum += i  # ჯამის დაგროვება

# შედეგის დაბეჭდვა
print(f"დიაპაზონის 0-დან {number}-მდე რიცხვების ჯამი არის: {total_sum}")