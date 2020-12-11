"""
Jon Zhang
run.py
"""
import sys
import json
import os
import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(0, 'src')
from src.data_analysis import *

### run go.bat
    # some function to do this

### run data analysis methods
def main(targets):
    """
    this method will run all the methods within data_analysis.py
    """
    # battery_config = json.load(open("config/battery-db-data-params.json"))
    # time_config = json.load(open("config/counters-ull-time-data-params.json"))
#     sqlserver_dc_config = [
#         {
#          'Trusted_Connection': 'yes', 'driver': '{SQL Server}',
#          'server': 'your_sql_server', 'database': 'test/testdata.db', 'user': 'your_db_username',
#          'password': 'your_db_password', 'autocommit': True
#         }
#     ]

    # if targets:

    # parse through data
    df = parse_data("data/temp/counters_ull_time_data.csv")

    # print statements
    print("Here is the max value of our battery life %: ")
    print(get_max_battery(df, "ID_INPUT", 1))
    print(" ")
    print("The value is 96%.")
    print(" ")
    print(" ")

    print("Here is the min value of our battery life %: ")
    print(get_min_battery(df, "ID_INPUT", 1))
    print(" ")
    print("The value is 61%.")
    print(" ")
    print(" ")

    print("Here is the mean value of our battery life %: ")
    print(get_mean_battery(df, "ID_INPUT", 1))
    print(" ")
    print("The value is 76.2738%.")
    print(" ")
    print(" ")

    cleaned_data = clean_data(df)

    print("Here's the graph displaying changes of battery life percentages: ")
    print(plot_battery_life(cleaned_data, 'Battery_life(%)'))
    print("Changes_of_battery_life.png")
    print(" ")

    print("Here's the graph displaying changes of AC Status: ")
    print(plot_ac_status(cleaned_data, 'AC'))
    print("AC_Status_png")


#     if 'time' in targets:
#         try:
#             df
#             # needs to be changed
#         except NameError:
#             # needs to be changed
#             df = pd.read_csv("data/temp/counters_ull_time_data.csv")

if __name__ == "__main__":
    targets = sys.argv[1:]
    main(targets)
