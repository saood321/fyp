#Import Libraries
from svmClasssifier import *
import xlwt
import math

def distance():

    book = xlwt.Workbook()
    sheet1 = book.add_sheet('Sheet1')
    df = pd.read_excel("random1.xls", sheet_name=0)

    list1 = list(df['T1'])
    list2 = list(df['T2'])

    def createList(r1, r2):
        return list(range(r1, r2))
    def createList1(r3, r4):
        return list(range(r3, r4))

    r1, r2 = 0, 68
    mylist1 = createList(r1, r2)
    r3, r4 = 0, 66
    mylist2 = createList1(r3, r4)

    sheet1.write(0, 0, 'Test')
    row = 0
    for i in mylist1:
        for j in mylist2:
            if j >= i:
                row = row + 1
                distance = math.sqrt(((list1[j + 1] - list1[i]) ** 2) + ((list2[j + 1] - list2[i]) ** 2))
                sheet1.write(row, 0, distance)

    name = "random3.xls"
    book.save(name)
    mood=predict()
    return mood
