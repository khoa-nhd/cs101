import random

answer = random.randint(0, 10)
print(answer)
print("To dang nghi den 1 so nguyen nam trong khoang 0 den 10.")
counter = 0
while counter < 3:
    soNao = int(input("Do ban biet to dang nghi den so nao? "))
    if soNao == answer:
        print ("Dung roi!")
        break
    elif soNao > answer:
        print ("Cao qua!")
    else:
        print ("Thap qua!")
        
    counter += 1