import os
from typing import List

from keras.models import Sequential, Model


MODEL_FILE_PATH = 'model.h5'


class ItemNet():
    model = Sequential()
    model.add(Dense(5, input_shape=(5,), use_bias=True, activation='sigmoid'))
    model.add(Dropout(0.1))
    model.add(Dense(5, activation='sigmoid', use_bias=True))
    model.add(Dropout(0.1))
    model.add(Dense(1, activation='linear', use_bias=True))
    return model


def load_model():
    model = ItemNet()

    model.compile(loss='mean_squared_error',
        optimizer=RMSprop(),
        metrics=['accuracy'])

    if os.path.exists(MODEL_FILE_PATH):
        model.load(MODEL_FILE_PATH)
    return model


def predict_item(item: Item):
    model = load_model()
    x, _ = item.to_vec()
    y = model.evaluate(x)
    return y


def learn_item(item: List[Item]):
    # FIXME: Concurrency
    model = load_model()
    x, y = item.to_vec()
    model.fit(x, y)
    model.save(MODEL_FILE_PATH)
