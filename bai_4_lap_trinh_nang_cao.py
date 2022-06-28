def favorite_song(songs, votes):
    lastSong = ""
    lastCount = 0
    
    for song in songs:
        counter = 0
        for vote in votes:
            if song == vote:
                counter = counter + 1
                if counter > lastCount:
                    lastSong = song
                    lastCount = counter
    return lastSong

songs = ["Believer", "Thunder"]
votes = ["Believer", "Believer", "Thunder","Believer","Thunder"]
favorite_song(songs, votes)
answer = favorite_song(songs, votes)
print(answer)