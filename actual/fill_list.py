
def fill(myresult,playlistBox,playlist):

    k = 0
    length = len(myresult)
    while k<length:
        playlistBox.insert(k, myresult[k][2])
        playlist.insert(k, myresult[k][2])
        k=k+1
    return playlistBox,playlist