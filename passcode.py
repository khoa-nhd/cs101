counter = 0
while counter < 3:
    passcode = input("Xin nhập vào mật khẩu: ")

    if passcode == "0042" or passcode == "2021":
        print("Chào mừng bạn đến với Siêu Máy Tính")
        break
    else:
        print("Mật khẩu sai!")

    counter = counter + 1