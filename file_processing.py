"""
CSE 163
Zachary Zhang

This file is used to perform joins and other
dataset modifcations accross multiple datasets.
"""
import pandas as pd
import pickle


def avocados_processing():
    """
    Used to modify 'avocados cleaned.csv'
    """
    dataset = pd.read_csv(
        './data/avocado cleaned.csv', index_col='Date', parse_dates=True
    )
    with open('./data/avocados_shp.df', 'wb') as f:
        pickle.dump(dataset, f)


def main():
    avocados_processing()


if __name__ == '__main__':
    main()
