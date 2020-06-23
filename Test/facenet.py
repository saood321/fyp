import numpy as np
from keras.models import load_model
from keras.preprocessing import image

model = load_model(r'Models\facenet_keras.h5')
print('hhh')
img = image.load_img('img.jpeg')
img = img.resize((160, 160))
face = np.asarray(img)
facep = face.astype('float32')
mean, std = facep.mean(), facep.std()
facep = (facep - mean) / std
samples = np.expand_dims(facep, axis=0)
preds = model.predict(samples)
print(preds)
