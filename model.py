import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR

def get_data(filename):
    dates = []
    prices = []
    with open(filename, 'r') as csvfile:
        csvReader = csv.reader(csvfile)
        for _ in range(3):
            next(csvReader, None)
        for row in csvReader:
            if not row or not row[0]:
                continue
            dates.append(int(row[0].split("-")[2]))
            prices.append(float(row[1]))
    return dates, prices

def predict_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates), 1))
    x = np.reshape(x, (1, -1))
    
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_rbf.fit(dates, prices)

    return svr_rbf.predict(x)
    
def run_prediction(csv_file):
    dates, prices = get_data(csv_file)
    next_day = dates[-1] + 1
    prediction = predict_prices(dates, prices, next_day)
    return float(prediction[0])