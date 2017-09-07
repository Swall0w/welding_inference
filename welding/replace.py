import pandas as pd


def add_hour(string):
    return "00:{}".format(string)


def _replace_one(string):
    string = list(string)
    string[1] = '1'
    return ''.join(string)


def iterative_hour_to_series(series):
    maxvalue = series.max()
    [maxindex] = series[series.str.contains(maxvalue)].index
    front = series[:(maxindex+1)]
    back = series[(maxindex+1):].apply(_replace_one).reset_index(drop=True)
    front = front.append(back, ignore_index=True)
    return front
