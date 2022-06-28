import random

print("Chung minh cung choi oan tu ti nhe!")

random_number = random.randint(0, 2)
print(random_number)
if random_number == 0:
    computer_choice = "keo"
elif random_number == 1:
    computer_choice = "bua"
else:
    computer_choice = "bao"
nguoiChoira = input("Ban ra gi? ")
if nguoiChoira == "bao":
    nguoiChoiraDoithanhSo = 2
print("May tinh ra " + computer_choice)
if nguoiChoiraDoithanhSo == random_number:
    print("Hoa roi!")