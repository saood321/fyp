import pandas as pd

import joblib
def predict():
    dd = pd.read_excel("random3.xls", sheet_name=0)
    Test = list(dd['Test'])
    filename = 'finalized_model.sav'
    loaded_model = joblib.load(filename)
    var = loaded_model.predict([Test])
    print(var)
predict()