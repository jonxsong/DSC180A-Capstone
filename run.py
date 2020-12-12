"""
Jon Zhang, Keshan Chen
run.py
"""
import sys
import json
import os
import pandas as pd
import matplotlib.pyplot as plt

sys.path.insert(0, 'src')
from src.data_exploration import *

def main(targets):
    """
    this method will run all the methods within class data_exploration.py
    """
    # parse through data
    df = data_exploration.parse_data("data/temp/counters_ull_time_data.csv")

    # Value expected from method get_max_battery
    print("Here is the max value of our battery life %: ")
    print(data_exploration.get_max_battery(df, "ID_INPUT", 1))
    print("\n")

    # Value expected from method get_min_battery
    print("Here is the min value of our battery life %: ")
    print(data_exploration.get_min_battery(df, "ID_INPUT", 1))
    print("\n")

    # Value expected from method get_mean_battery
    print("Here is the mean value of our battery life %: ")
    print(data_exploration.get_mean_battery(df, "ID_INPUT", 1))
    print("\n")

    # data with indices reset based on ID_INPUT, stored into cleaned_data
    cleaned_data = data_exploration.clean_data(df)

    # Line Graph of Battery Life Percentages
    print("Here's the graph displaying changes of battery life percentages: ")
    print(data_exploration.plot_battery_life(cleaned_data, 'Battery_life(%)'))
    print("Please check the file path -> data/out/Changes_of_battery_life.png")

    print("\n")

    # Line Graph of the changes in AC Status
    print("Here's the graph displaying changes of AC Status: ")
    print(data_exploration.plot_ac_status(cleaned_data, 'AC'))
    print("Please check the file path -> data/out/Changes_of_AC_Status.png")

#     if 'time' in targets:
#         try:
#             df
#             # needs to be changed
#         except NameError:
#             # needs to be changed
#             df = pd.read_csv("data/temp/counters_ull_time_data.csv")

#     battery_config = json.load(open("config/battery-db-data-params.json"))
#     time_config = json.load(open("config/counters-ull-time-data-params.json"))
#     sqlserver_dc_config = [
#         {
#          'Trusted_Connection': 'yes', 'driver': '{SQL Server}',
#          'server': 'your_sql_server', 'database': 'test/testdata.db', 'user': 'your_db_username',
#          'password': 'your_db_password', 'autocommit': True
#         }
#     ]

if __name__ == "__main__":
    targets = sys.argv[1:]
    main(targets)
