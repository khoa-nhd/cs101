def findmax(x, y):
  if x >= y :
    return x
  else :
    return y

def num(y):
  x = int(input("nhap so "))
  while x >= y:
    x = int(input("nhap lai "))
  return (x)


print("Toi se tim so lon nhat cho ban. Ban vui long nhap so.")

a = num(10)
b = num(15)
c = num(20)


result = findmax(findmax(a, b), findmax(b, c))
print(result)






