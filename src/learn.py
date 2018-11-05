import os
from typing import List


from keras.optimizers import RMSprop
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout
import numpy as np

from models.item import Item


MODEL_FILE_PATH = 'model.h5'


def ItemNet():
    model = Sequential()
    model.add(Dense(5, input_shape=(5,), use_bias=True, activation='sigmoid'))
    model.add(Dropout(0.1))
    model.add(Dense(5, activation='sigmoid', use_bias=True))
    model.add(Dropout(0.1))
    model.add(Dense(1, activation='linear', use_bias=True))
    return model


def get_model():
    if os.path.exists(MODEL_FILE_PATH):
        return load_model(MODEL_FILE_PATH)
    model = ItemNet()
    model.compile(loss='mean_squared_error',
        optimizer=RMSprop(),
        metrics=['accuracy'])
    return model


def predict_item(item: Item):
    model = get_model()
    x, _ = item.to_vec()
    y = model.predict(np.array([x]))
    return float(y[0])


def learn_item(item: List[Item]):
    # FIXME: Concurrency
    model = get_model()
    x, y = item.to_vec()
    model.fit(np.array([x]), np.array([y]))
    model.save(MODEL_FILE_PATH)
