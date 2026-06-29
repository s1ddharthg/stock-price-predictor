import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR

dates = []
prices = []



def get_data(filename):
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
    
    plt.scatter(dates, prices, color = 'black', label = 'Data')
    plt.plot(dates, svr_rbf.predict(dates), color='blue', label='RBF SVR')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('SVR')
    plt.legend()
    plt.show()
    return svr_rbf.predict(x)
    
get_data('AAPL_historical_data.csv')
predicted_price = predict_prices(dates, prices, 29)

print(predicted_price)