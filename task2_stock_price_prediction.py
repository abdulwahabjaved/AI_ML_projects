

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


stock_symbol = 'AAPL'

df = yf.download(stock_symbol, start='2020-01-01', end='2024-01-01')

print("🔹 Data Head:")
print(df.head())




X = df[['Open', 'High', 'Low', 'Volume']]


df['Next_Close'] = df['Close'].shift(-1)
y = df['Next_Close']


X = X[:-1]
y = y[:-1]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)


# I use the Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)



lr_pred = lr_model.predict(X_test)
rf_pred = rf_model.predict(X_test)


plt.figure(figsize=(12,6))

plt.plot(y_test.values, label='Actual Price')
plt.plot(lr_pred, label='Linear Regression Prediction')
plt.plot(rf_pred, label='Random Forest Prediction')

plt.title(f"{stock_symbol} Stock Price Prediction")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()

plt.show()



last_data = X.tail(1)

lr_next = lr_model.predict(last_data)
rf_next = rf_model.predict(last_data)

print("\n🔮 Next Day Prediction:")
print("Linear Regression:", lr_next[0])
print("Random Forest:", rf_next[0])