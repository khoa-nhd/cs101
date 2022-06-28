def chan_hay_le(array):
    mangDeSuDungTronHamKhac = []
    dapAn1 = 0
    dapAn1 = len(array) % 2
    if dapAn1 == 0:
        chanHayLe = "chan"
    else:
        chanHayLe = "le"
    return chanHayLe

def find_median(array):
    if len(array) == 0:
        return
    chanHayLe = chan_hay_le(array)
    dapAn = 0
    if chanHayLe == "le":
        dapAn2 = round(((len(array) + 1) / 2) - 1)
        return (array[dapAn2])
    else:
        dapAn2 = round(len(array) / 2 - 1)
        dapAn3 = round(len(array) / 2)
        dapAn = ((array[dapAn2]) + (array[dapAn3])) / 2
        print(dapAn)
    return dapAn
            

array = [2, 4, 5, 7, 8, 9]
a = find_median(array)
print(a)