import pandas as pd
import joblib
import os

def predict():
    dd = pd.read_excel("random3.xls", sheet_name=0)
    Test = list(dd['Test'])
    filename = 'myModel.sav'
    loaded_model = joblib.load(filename)
    var = loaded_model.predict([Test])
    return var



