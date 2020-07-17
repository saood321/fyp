import actual.DataBaseConnect
mydb,mycursor=actual.DataBaseConnect.database()

def historysongs(songtype,val,limit):
    if songtype==None:
        sql = ("""SELECT history.SongId FROM history INNER JOIN song ON history.SongId = song.SongId WHERE  history.UserId='%s' ORDER BY Rating DESC LIMIT %s""" % (val, limit))
    else:
        sql = ( """SELECT history.SongId FROM history INNER JOIN song ON history.SongId = song.SongId WHERE song.SongTypeId='%s' and history.UserId='%s' ORDER BY Rating DESC LIMIT %s""" % (songtype,val,limit))
    mycursor.execute(sql)
    history = mycursor.fetchall()
    print(history)
    return history

def ratedsong(songtype):
    sql = ("""SELECT SongId FROM song  WHERE SongTypeId='%s' ORDER BY TotalRating DESC LIMIT 3 """ % (songtype))
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult

def randomsong(songtype,random_no):
    sql = ("""SELECT SongId FROM song WHERE SongTypeId='%s' ORDER BY RAND() LIMIT %s """ % (songtype, random_no))
    mycursor.execute(sql)
    randomlist = mycursor.fetchall()
    return randomlist

def repeatationcheck(combine_list):


    i = 0
    repeat_list=[]
    while i < 9:
        j = i+1
        while j < 10 :

            if (combine_list[i][0] == combine_list[j][0]) and combine_list[i][0] not in repeat_list:
                repeat_list.append(combine_list[i][0])

            j = j + 1
        i=i+1

    return repeat_list
def remove_repeation(combine_list,repeat_list,repeation,type):
    sql = ("""SELECT SongId FROM song WHERE SongTypeId='%s' ORDER BY RAND() LIMIT %s """ % (type, repeation))
    mycursor.execute(sql)
    randomlist = mycursor.fetchall()
    #combine_list=list(combine_list)
    print(combine_list)
    s=0
    t=0
    for i in enumerate(combine_list):
        print(i )

def calculate_size(data_set, size=0):
    for i in data_set:
        if isinstance(i, tuple) or isinstance(i, list):
            size += calculate_size(i)
        else:
            size += 1
    return size

def appending(combine_list,new_list):
    count=0
    for i in new_list:

        r=0
        for j in combine_list:
            if i==j:
                r=2
        if(r==0):
            combine_list.append(i)
            count = count + 1

    return combine_list

def database(mood,val):
    global myresult

    import CheckSongType
    songtype1=CheckSongType.songtype(mood)
    songtype=songtype1[0][0]
    history=historysongs(songtype,val,3)
    myresult=ratedsong(songtype)
    random_no = 10 - 3 - len(history)
    randomlist=randomsong(songtype,random_no)
    combine_list=[]
    combine_list=appending(combine_list,myresult)
    combine_list=appending(combine_list,history)
    combine_list=appending(combine_list,randomlist)


    less=len(combine_list)
    less=10-less

    while less>0:
        a = randomsong(songtype, (less))
        combine_list=appending(combine_list,a)
        less = len(combine_list)
        less = 10 - less

    """
    if less>0:
        a=randomsong(type, (less))
        print(a)

        while less>0:
            combine_list.append(a[less-1])
            less=less-1
        print(combine_list)
    #repeat_list=repeatationcheck(combine_list)
    #repeation=calculate_size(repeat_list)
    #print(repeation,repeat_list)
  
    if repeation>0:
        remove_repeation(combine_list,repeat_list,repeation,type)
        """

    return combine_list





