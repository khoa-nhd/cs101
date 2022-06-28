def who_is_winner(votes):
    dapAn = 0
    trauVote = 0
    williamVote = 0
    for x in votes:
        if x == "Trau":
            trauVote = trauVote + 1
        else:
            williamVote = williamVote + 1
    if williamVote == trauVote:
        dapAn = "Both"
        return dapAn
    elif trauVote > williamVote:
        dapAn = "Trau"
        return dapAn
    else:
        dapAn = "William"
        return dapAn
    
votes = ["William,William,William,William,Trau,Trau,Trau"]
answer = who_is_winner(votes)
print(answer)