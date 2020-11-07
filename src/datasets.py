"""
Jon Zhang
datasets.py
"""
import numpy as np
import pandas as pd

""" Parser """
def parseData(fname):
    for l in open(fname)
        yield eval(l)

data = list(parseData("data/temp/counters_ull_time_data.csv"))
df = pd.DataFrame(data)
