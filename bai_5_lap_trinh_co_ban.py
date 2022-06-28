def filter(array):
    dapAn = []
    for nguoi in array:
        x = nguoi.split(",")
        if x[2] == "Hanoi":
            dapAn.append(nguoi)
    print(dapAn)
    return dapAn

array = ["01,quan,Hanoi", "02,tri,HCM", "03,nam,Hanoi"]
filter(array)