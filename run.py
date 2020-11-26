"""
Jon Zhang
run.py
"""
import sys
import json
import os
import pandas as pd

sys.path.insert(0, 'src')
from src.data_analysis import *

### run go.bat
    # some function to do this

### run data analysis methods
def main(targets):
    """
    this method will run all the methods within data_analysis.py
    """
    battery_config = json.load(open('config/battery-db-data-params.json'))
    time_config = json.load(open('config/counters-ull-time-data-params.json'))

    if 'battery' in targets:

        # parse through data
        df = parse_data("data/temp/counters_ull_time_data.csv")

        # print statements
        print("Here is the max value of our battery life %: ")
        print(get_max_battery(df, "ID_INPUT", 2))
        print(" ")
        print("The value is 63%.")
        print(" ")
        print(" ")

        print("Here is the min value of our battery life %: ")
        print(get_min_battery(df, "ID_INPUT", 2))
        print(" ")
        print("The value is 26%.")
        print(" ")
        print(" ")

        print("Here is the mean value of our battery life %: ")
        print(get_mean_battery(df, "ID_INPUT", 2))
        print(" ")
        print("The value is 44.5%.")
        print(" ")
        print(" ")

    if 'time' in targets:
        try:
            df
            # needs to be changed
        except NameError:
            # needs to be changed
            df = pd.read_csv("data/temp/counters_ull_time_data.csv")

if __name__ == "__main__":
    targets = sys.argv[1:]
    main(targets)
