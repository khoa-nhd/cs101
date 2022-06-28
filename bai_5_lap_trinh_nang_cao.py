import random

def filter(array):
    dapAn = []
    for nguoi in array:
        x = nguoi.split(",")
        if x[2].strip() == "Hanoi":
            dapAn.append(nguoi)
    return dapAn

def filter_random(array):  
    x = filter(array)
    if len(x) <= 3:
        return x
    else:
        dapAnKhiCoNhieuHon3PhanTu = []
        while len(dapAnKhiCoNhieuHon3PhanTu) < 3: 
            y = (random.randint(0, len(x) - 1))
            item = x.pop(y)
            dapAnKhiCoNhieuHon3PhanTu.append(item)
        return dapAnKhiCoNhieuHon3PhanTu

array = ['07, duc, Hanoi', '01, nga, Hanoi', '06, nam, Hanoi', '03, giang, HCM', '04, thuy, Hanoi', '02, quan, Hanoi', '08, dung, Hanoi', '09, quang, HCM']
dapAn = filter_random(array)
print(dapAn)