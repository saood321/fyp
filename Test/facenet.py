import numpy as np
from keras.models import load_model
from keras.preprocessing import image

model = load_model('facenet_keras.h5')
img = image.load_img('123.jpg')
img = img.resize((160, 160))
face = np.asarray(img)
facep = face.astype('float32')
mean, std = facep.mean(), facep.std()
facep = (facep - mean) / std
samples = np.expand_dims(facep, axis=0)
print(samples)
preds = model.predict(samples)
print(preds)
