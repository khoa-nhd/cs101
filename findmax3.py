def findmax(x, y):
  if x >= y :
    return x
  else :
    return y


print("Toi se tim so lon nhat cho ban. Ban vui long nhap so.")
a = int(input("nhap so "))
while a >= 10:
  a = int(input("nhap lai "))
b = int(input("nhap so "))
while b >= 10:
  b = int(input("nhap lai "))
c = int(input("nhap so "))
while c >= 10:
  c = int(input("nhap lai "))


result = findmax(findmax(a, b), findmax(b, c))
print(result)