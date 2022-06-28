data = [
[10, 62, 30, 65], 
[100, 100], 
[86, 85, 87]
]
result = []
for x in data:
    if len(x) < 3:
        result.append(0.0)
    else:
        total = 0
        nhoHon50 = 0
        for y in x:
            total = total + y
            if y < 50:
                nhoHon50 = 1
        if nhoHon50 == 1:
            result.append(0.0)
        else:
            result.append(total / len(x))
print(result)
