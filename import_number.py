#!?usr/bin/python3

from pandas import read_excel


def importPhone(filepath):
    df = read_excel(filepath, 0)
    for index, (data) in df.iterrows():
        print(data)