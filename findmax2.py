def findmax(x, y):
  if x >= y :
    return x
  else :
    return y


print("Toi se tim so lon nhat cho ban. Ban vui long nhap so.")
a = input("nhap so ")
b = input("nhap so ")
c = input("nhap so ")


result = findmax(findmax(a, b), findmax(b, c))
print(result)