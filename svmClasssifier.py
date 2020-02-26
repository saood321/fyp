import pandas as pd
from sklearn import svm
import numpy as np

def predict():
    df = pd.read_excel("distance.xlsx", sheet_name=0)
    dd = pd.read_excel("random3.xls", sheet_name=0)
    list1 = list(df['H1'])
    list2 = list(df['H2'])
    list3 = list(df['H3'])
    list4 = list(df['H4'])
    list5 = list(df['H5'])

    list10 = list(df['SA1'])
    list11 = list(df['SA2'])
    list12 = list(df['SA3'])
    list13 = list(df['SA4'])
    list14 = list(df['SA5'])

    list17 = list(df['SU1'])
    list18 = list(df['SU2'])
    list19 = list(df['SU3'])
    list20 = list(df['SU4'])
    list21 = list(df['SU5'])


    X = np.array([list1, list2, list3, list4, list5, list10, list11, list12, list13, list14, list17, list18, list19, list20,list21])

    y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    clf = svm.SVC(kernel='linear', C=1.0)
    clf.fit(X, y)
    Test = list(dd['Test'])
    var = clf.predict([Test])
    if var == 0:
        print("Happy mood")
    elif var == 1:
        print("Sad Mood")
    elif var == 2:
        print("Surprise")
