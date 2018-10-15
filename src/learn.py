from keras.models import Sequential, Model


def ItemModel():
    model = Sequential()
    model.add(Dense(5,  input_shape=(5,), use_bias=True, activation='sigmoid'))
    model.add(Dropout(0.1))
    model.add(Dense(5, activation='sigmoid', use_bias=True))
    model.add(Dropout(0.1))
    model.add(Dense(1, activation='linear', use_bias=True))
    return model


