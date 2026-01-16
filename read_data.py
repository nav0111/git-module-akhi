import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

data_url = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv'
def read_and_visualize(url):
    df = pd.read_csv(url)
    print(df.shape[0])
    print(df.shape[1])
    days = pd.to_datetime(df['AAPL_x'])
    plt.figure(figsize=(10,6))
    plt.plot(days, df['AAPL_y'])
    plt.title("Closing Prices over Time")
    plt.xlabel('Days')
    plt.ylabel('price')
    plt.savefig('apple_stock.png')
    plt.show()
    return df

read_and_visualize(data_url)



