import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

data_url = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv'

#Simple moving average function
def calculate_moving_average(df, window_size=30, column = 'AAPL_y'):
    sma = df['AAPL_y'].rolling(window = window_size).mean()
    return sma

def read_and_visualize(url):
    df = pd.read_csv(url)
    Moving_average = calculate_moving_average(df, window_size=30)
    print(df.shape[0])
    print(df.shape[1])
    days = pd.to_datetime(df['AAPL_x'])
    plt.figure(figsize=(10,6))
    plt.plot(days, df['AAPL_y'], color ='green', label =  f'aily closing price')
    plt.plot(days, Moving_average, color = 'red', label = f'daily moving average')
    plt.title("Closing Prices over Time with daily moving average")
    plt.xlabel('Days')
    plt.ylabel('price')
    plt.savefig('apple_stock.png')
    plt.show()
    return df

read_and_visualize(data_url)



