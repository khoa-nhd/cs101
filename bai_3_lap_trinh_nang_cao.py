so = 0
chu = ""
kiTu = ""
dapAn = ""
for kiTu in plaintext:
    if kiTu == "Y":
        dapAn = dapAn + "A"
    elif kiTu == "y":
        dapAn = dapAn + "a"
    elif kiTu == "Z":
        dapAn = dapAn + "B"
    elif kiTu == "z":
        dapAn = dapAn + "b"
    else:
        so = ord(kiTu) + 2
        chu = chr(so)
        dapAn = dapAn + (chu)
print(str(dapAn))