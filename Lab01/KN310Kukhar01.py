import pandas as pd
from Lab01.KN310Kukhar02 import *


def parse_data():
    df = pd.read_csv('Lab01/DATABASE.csv', sep=';', decimal=",")
    df.rename(columns={'day/month': 'Date'}, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'] + '.2019', format='%d.%b.%Y')
    df['Time'] = pd.to_datetime(df['Time']).dt.strftime('%H:%M:%S')

    for r in range(len(df)):
        df.at[r, 'Humidity'] = float(int(df.at[r, 'Humidity'][:-1]) / 100)
        df.at[r, 'Wind Speed'] = int(df.at[r, 'Wind Speed'][:-4])
        df.at[r, 'Wind Gust'] = int(df.at[r, 'Wind Gust'][:-4])

    return df


def main():
    data = parse_data()
    draw_plots(data)


if __name__ == '__main__':
    main()
