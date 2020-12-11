"""
Jon Zhang
data_analysis.py
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def parse_data(fname):
    """
    Description
    Parameters
    Returns
    """
    return pd.read_csv(fname)

def clean_data(data):
    """
    """
    ac_status = data.loc[(data['ID_INPUT'] == 0)].reset_index()
    battery_life = data.loc[(data['ID_INPUT'] == 1)].reset_index()
    battery_saver = data.loc[(data['ID_INPUT'] == 2)].reset_index()
    battery_time = data.loc[(data['ID_INPUT'] == 3)].reset_index()

    d = {'AC': ac_status['VALUE'], 'Battery_life(%)': battery_life['VALUE'],
    'Battery_saver': battery_saver['VALUE'], 'Battery_time(seconds)': battery_time['VALUE']}

    new_data = pd.DataFrame(d)
    return new_data

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

def plot_battery_life(data, column):
    """
    """
    x = list(data.index)
    y = data[column]
    plt.figure(1)
    plt.plot(x, y)
    plt.title("Changes of battery_life(%)")
    plt.xlabel('index')
    plt.ylabel('battery_life(%)')
    return plt.savefig("Changes_of_battery_life.png")

def plot_ac_status(data, column):
    """
    """
    x = list(data.index)
    y = data[column]
    plt.figure(2)
    plt.plot(x, y)
    plt.title('Changes of AC Status')
    plt.xlabel('index')
    plt.ylabel('AC Status')
    return plt.savefig("AC_Status.png")
