import pandas as pd
from sklearn import svm
import numpy as np
import joblib
def predict():
    dd = pd.read_excel("random3.xls", sheet_name=0)
    Test = list(dd['Test'])
    filename = 'final_model.sav'
    loaded_model = joblib.load(filename)
    var = loaded_model.predict([Test])
    print(var)