import DataBaseConnect
mydb,mycursor=DataBaseConnect.database()

def historysongs(type):
    sql = ("""SELECT history.SongId FROM history INNER JOIN song ON history.SongId = song.SongId WHERE song.SongTypeId='%s' """ % (type))
    mycursor.execute(sql)
    history = mycursor.fetchall()
    return history

def ratedsong(type):
    sql = ("""SELECT SongId FROM song  WHERE SongTypeId='%s' ORDER BY TotalRating DESC LIMIT 3 """ % (type))
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def randomsong(type,random_no):
    sql = ("""SELECT SongId FROM song WHERE SongTypeId='%s' ORDER BY RAND() LIMIT %s """ % (type, random_no))
    mycursor.execute(sql)
    randomlist = mycursor.fetchall()
    return randomlist

def repeatationcheck(combine_list):
    repeation = 0
    i = 0

    while i < 10:
        j = i+1
        while j < 10 :

            if (combine_list[i][0] == combine_list[j][0]):
                repeation = repeation + 1
            j = j + 1
        i=i+1

    return repeation

def database(mood):
    global myresult
    if mood=="Happy":
        type=1

    history=historysongs(type)
    myresult=ratedsong(type)
    random_no = 10 - 3 - len(history)
    randomlist=randomsong(type,random_no)


    """
    sql = ("SELECT COUNT(*) FROM song WHERE SongTypeId='%s' "% (type))
    mycursor.execute(sql)
    count = mycursor.fetchall()
    """
    combine_list=history+myresult+randomlist
    repeation=repeatationcheck(combine_list)
    if repeation==0:
        return combine_list

    else:
        database(mood)




