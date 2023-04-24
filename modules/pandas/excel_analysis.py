"""
learn how to use pandas module.

Reference:
    - https://www.learncodewithmike.com/2020/11/python-pandas-dataframe-tutorial.html
"""
import pandas as pd

if __name__ == '__main__':
    # read the CSV file into a Pandas DataFrame
    df = pd.read_csv('modules/pandas/addresses.csv')

    # print the first few rows of the DataFrame
    print('----show dataframe----')
    print(df)
    
    print(df.head()) # get several data.
    print(df.tail()) # get the last data.