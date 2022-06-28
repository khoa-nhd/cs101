def calculate_score(trials):
    inRa = 0
    dapAn = 0
    if(len(trials) == 0):
        return inRa
    for x in trials:
        dapAn = dapAn + x
        inRa = dapAn / len(trials)
    return inRa
    
trials = [1,2,3,4]
answer = calculate_score(trials)
print (answer)
