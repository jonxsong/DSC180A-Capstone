"""
Jon Zhang
data_analysis.py
"""
import numpy as np
import pandas as pd

def parse_data(fname):
    """
    Description
    Parameters
    Returns
    """
    return pd.read_csv(fname)

def get_max_battery(data, column, value):
    """
    Description
    Parameters
    Returns
    """
    return data.loc[(data[column] == value)].max()

def get_min_battery(data, column, value):
    """
    Description
    Parameters
    Returns
    """
    return data.loc[(data[column] == value)].min()

def get_mean_battery(data, column, value):
    """
    Description
    Parameters
    Returns
    """
    return data.loc[(data[column] == value)].mean()
