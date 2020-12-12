"""
Jon Zhang, Keshan Chen
data_exploration.py
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class data_exploration():
    """
    class data_exploration contains all the relevant methods for data exploration.
    """

    def parse_data(fname):
        """
        Description: reads a csv file and converts into dataframe
        Parameters: fname -> .csv
        Returns: DataFrame
        """
        return pd.read_csv(fname)

    def clean_data(data):
        """
        Description: resets original data indices by the id input value
        Parameters: data -> DataFrame Object
        Returns: DataFrame
        """
        ac_status = data.loc[(data['ID_INPUT'] == 0)].reset_index()
        battery_life = data.loc[(data['ID_INPUT'] == 1)].reset_index()
        battery_saver = data.loc[(data['ID_INPUT'] == 2)].reset_index()
        battery_time = data.loc[(data['ID_INPUT'] == 3)].reset_index()

        re_index = {'AC': ac_status['VALUE'],
             'Battery_life(%)': battery_life['VALUE'],
             'Battery_saver': battery_saver['VALUE'],
             'Battery_time(seconds)': battery_time['VALUE']}

        new_data = pd.DataFrame(re_index)
        return new_data

    def get_max_battery(data, column, value):
        """
        Description: returns the max battery percentage
        Parameters: data -> DataFrame, column -> Series Object, value -> Integer
        Returns: Max Value -> Integer
        """
        return data.loc[(data[column] == value)].max()

    def get_min_battery(data, column, value):
        """
        Description: returns the min battery percentage
        Parameters: data -> DataFrame, column -> Series Object, value -> Integer
        Returns: Min Value -> Integer
        """
        return data.loc[(data[column] == value)].min()

    def get_mean_battery(data, column, value):
        """
        Description: returns the mean battery percentage
        Parameters: data -> DataFrame, column -> Series Object, value -> Integer
        Returns: Mean Value -> Integer
        """
        return data.loc[(data[column] == value)].mean()

    def plot_battery_life(data, column):
        """
        Description: plots a line graph of the battery life percentages.
        Parameters: data -> DataFrame, column -> Series Object
        Returns: Changes_of_battery_life.png -> file saved in root directory
        """
        x = list(data.index)
        y = data[column]
        plt.figure(1)
        plt.plot(x, y)
        plt.title("Changes of battery_life(%)")
        plt.xlabel('index')
        plt.ylabel('battery_life(%)')
        #return plt.show()
        return plt.savefig("data/out/Changes_of_battery_life.png")

    def plot_ac_status(data, column):
        """
        Description: plots a line graph of the AC Status.
        Parameters: data -> DataFrame, column -> Series Object
        Returns: Changes_of_AC_Status.png -> file saved in root directory
        """
        x = list(data.index)
        y = data[column]
        plt.figure(2)
        plt.plot(x, y)
        plt.title('Changes of AC Status')
        plt.xlabel('index')
        plt.ylabel('AC Status')
        #return plt.show()
        return plt.savefig("data/out/Changes_of_AC_Status.png")
