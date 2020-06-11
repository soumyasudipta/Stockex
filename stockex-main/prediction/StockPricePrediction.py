# IMPORTING IMPORTANT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import math
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
import prediction.preprocessing as preprocessing
import yfinance as yf
import mongodb.database_manager as mdb

def predict_next(data,symbol):
    # IMPORTING DATASET 
    dataset = data
    # dataset = dataset.reindex(index = dataset.index[::-1])

    # CREATING OWN INDEX FOR FLEXIBILITY
    obs = np.arange(1, len(dataset) + 1, 1)

    # TAKING DIFFERENT INDICATORS FOR PREDICTION
    OHLC_avg = dataset.mean(axis = 1)
    HLC_avg = dataset[['High', 'Low', 'Close']].mean(axis = 1)
    close_val = dataset[['Close']]

    # PREPARATION OF TIME SERIES DATASE
    OHLC_avg = np.reshape(OHLC_avg.values, (len(OHLC_avg),1)) # 1664
    scaler = MinMaxScaler(feature_range=(0, 1))
    OHLC_avg = scaler.fit_transform(OHLC_avg)

    # TRAIN-TEST SPLIT
    train_OHLC = int(len(OHLC_avg) * 0.75)
    test_OHLC = len(OHLC_avg) - train_OHLC
    train_OHLC, test_OHLC = OHLC_avg[0:train_OHLC,:], OHLC_avg[train_OHLC:len(OHLC_avg),:]

    # TIME-SERIES DATASET (FOR TIME T, VALUES FOR TIME T+1)
    trainX, trainY = preprocessing.new_dataset(train_OHLC, 1)
    testX, testY = preprocessing.new_dataset(test_OHLC, 1)

    # RESHAPING TRAIN AND TEST DATA
    trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
    testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
    step_size = 1

    # LSTM MODEL
    model = Sequential()
    model.add(LSTM(32, input_shape=(1, step_size), return_sequences = True))
    model.add(LSTM(16))
    model.add(Dense(1))
    model.add(Activation('linear'))

    # MODEL COMPILING AND TRAINING
    model.compile(loss='mean_squared_error', optimizer='adagrad') # Try SGD, adam, adagrad and compare!!!
    model.fit(trainX, trainY, epochs=5, batch_size=1, verbose=2)

    # PREDICTION
    trainPredict = model.predict(trainX)
    testPredict = model.predict(testX)

    # DE-NORMALIZING FOR PLOTTING
    trainPredict = scaler.inverse_transform(trainPredict)
    trainY = scaler.inverse_transform([trainY])
    testPredict = scaler.inverse_transform(testPredict)
    testY = scaler.inverse_transform([testY])

    # PREDICT FUTURE VALUES
    last_val = testPredict[-1]
    last_val_scaled = last_val/last_val
    next_val = model.predict(np.reshape(last_val_scaled, (1,1,1)))
    print("Last Day Value:", np.asscalar(last_val))
    print("Next Day Value:", np.asscalar(last_val*next_val))

    mdb.update_collection('stockex','prediction',symbol,np.asscalar(last_val*next_val))