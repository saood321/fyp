import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import pickle
def fun():
    data=pd.read_csv('train.csv')
    X=data.drop(['Class'],axis=1)
    y=data['Class']

    classifier=svm.SVC(kernel='linear')
    model=classifier.fit(X,y)
    filename = 'final_model.sav'
    pickle.dump(model, open(filename, 'wb'))


fun()