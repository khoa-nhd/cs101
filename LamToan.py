def tongHieu(): # Toán tổng hiệu
    tong = input("Tổng là: ")
    hieu = input("Hiệu là: ")
    soBe = (int(tong) - int(hieu)) / 2
    soLon = (int(tong) + int(hieu)) / 2
    print("Số bé là: " + str(soBe))
    print("Số lớn là: " + str(soLon))

def tongTi(): # Toán tổng tỉ
    tong = input("Tổng là: ")
    TiSoCuaSoBeLa = input("Tỉ số của số bé là: ")
    TiSoCuaSoLonLa = input("Tỉ số của số lớn là: ")
    TongSoPhanLa = int(TiSoCuaSoBeLa) + int(TiSoCuaSoLonLa)
    soBe = int(tong) / TongSoPhanLa * int(TiSoCuaSoBeLa)
    soLon = int(tong) - soBe
    print("Số bé là: " + str(soBe))
    print("Số lớn là: " + str(soLon))

def hieuTi(): # Toán hiệu tỉ
    hieu = input("Hiệu là: ")
    TiSoCuaSoBeLa = input("Tỉ số của số bé là: ")
    TiSoCuaSoLonLa = input("Tỉ số của số lớn là: ")
    HieuSoPhanLa = int(TiSoCuaSoLonLa) - int(TiSoCuaSoBeLa)
    soBe = int(hieu) / HieuSoPhanLa * int(TiSoCuaSoBeLa)
    soLon = int(hieu) + soBe
    print("Số bé là: " + str(soBe))
    print("Số lớn là: " + str(soLon))
    
toanGi = input("Bạn muốn làm toán gì: ") # Hỏi xem làm toán gì
if toanGi == "Tổng hiệu":
    tongHieu()
elif toanGi == "Tổng tỉ":
    tongTi()
elif toanGi == "Hiệu tỉ":
    hieuTi()