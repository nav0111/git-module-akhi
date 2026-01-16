
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

data_url = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv'

def read_and_visualize(url):
    df = pd.read_csv(url)
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    
    days = pd.to_datetime(df['AAPL_x'])
    
    plt.figure(figsize=(10,6))
    plt.plot(days, df['AAPL_y'])
    plt.title("Apple Stock Closing Prices over Time (2014)")
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    
    # Rotate date labels for better readability
    plt.xticks(rotation=45)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    plt.savefig('apple_stock.png', dpi=100)
    plt.show()
    
    return df

read_and_visualize(data_url)

