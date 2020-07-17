#Import libraries
import xlwt
from getLandmarks import *
from distanceCalculation import *
def landmarks(resized):
    book = xlwt.Workbook()
    sheet1 = book.add_sheet('sheet1')
    xlist, ylist = get_landmarks(resized)

    #saving x-axies points in excel from xlist
    for i, e in enumerate(xlist):
        sheet1.write(i, 0, e)
    name = "random1.xls"
    book.save(name)

    # saving y-axies points in excel from ylist
    for i, e in enumerate(ylist):
        sheet1.write(i, 1, e)
    name = "random1.xls"
    book.save(name)
    return distance()