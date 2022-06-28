def get_average_score(profiles):
    diem = []
    tong = 0
    trungBinhCong = 0
    for x in profiles:
        coPhaiLaDiem = x["score"]
        diem.append(coPhaiLaDiem)
    for phanTu in diem:
        tong = tong + phanTu
    trungBinhCong = tong/ len(diem)
    print(trungBinhCong)
    return trungBinhCong

profiles = [{'name': 'Trau', 'score': 8},
 	    {'name': 'Tre', 'score': 9},
 	    {'name': 'Tran', 'score': 9},
 	    {'name': 'Tri', 'score': 8}]
get_average_score(profiles)