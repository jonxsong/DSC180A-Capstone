"""
Jon Zhang, Keshan Chen, Vince Wong
data_exploration.py
"""
import sys
import json
import os
import pandas as pd
import numpy as np
from numpy import array
from numpy import argmax
import seaborn as sns
from functools import reduce
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.linear_model import SGDClassifier

class data_exploration():
    """
    class data_exploration contains all the relevant methods for data exploration.
    """

    def parse_cpu_data(fname):
        """
        Description: reads a csv file and converts into dataframe
        Parameters: fname -> .csv
        Returns: DataFrame
        """
        return pd.read_csv(fname, usecols=['guid','load_ts', 'batch_id',
                                           'name','instance','nrs', 'mean',
                                           'histogram_min', 'histogram_max','metric_max_val'],
                                  nrows=1000000,
                                  sep='\t')

    def parse_sys_data(fname):
        """
        Description: reads a csv file and converts into dataframe
        Parameters: fname -> .csv
        Returns: DataFrame
        """
        return pd.read_csv(fname, usecols=['guid','chassistype', 'modelvendor_normalized',
                                           'model_normalized', 'ram',
                                           'os','#ofcores', 'age_category',
                                           'graphicsmanuf', 'gfxcard', 'graphicscardclass',
                                           'processornumber', 'cpuvendor', 'cpu_family',
                                           'discretegraphics', 'vpro_enabled','persona'],
                                  sep=chr(1))

    def optimize_dataframe(df):
        """
        Description: takes in the cpu dataframe and optimizes it through converting columns
        Parameters: df -> DataFrame
        Returns: DataFrame
        """
        df_int = df.select_dtypes(include=['int'])
        converted_int = df_int.apply(pd.to_numeric, downcast='unsigned')
        compare_ints = pd.concat([df_int.dtypes, converted_int.dtypes], axis=1)

        df_float = df.select_dtypes(include=['float'])
        converted_float = df_float.apply(pd.to_numeric, downcast='float')
        compare_floats = pd.concat([df_float.dtypes,converted_float.dtypes], axis=1)

        optimized_df = df.copy()
        optimized_df[converted_int.columns] = converted_int
        optimized_df[converted_float.columns] = converted_float
        df_obj = df.select_dtypes(include=['object']).copy()

        converted_obj = pd.DataFrame()

        for col in df_obj.columns:
            num_unique_values = len(df_obj[col].unique())
            num_total_values = len(df_obj[col])
            if num_unique_values / num_total_values < 0.5:
                converted_obj.loc[:,col] = df_obj[col].astype('category')
            else:
                converted_obj.loc[:,col] = df_obj[col]

        optimized_df[converted_obj.columns] = converted_obj
        return optimized_df

    def get_cpu_statistics(df, column, value):
        """
        Description: returns the dataframe when the column 'name' is that specified
        Parameters: df -> DataFrame
        Returns: DataFrame
        """
        return df.loc[df[column] == value]

    def get_guid(df, column):
        """
        Description: returns a list consisting of all the guid's
        Parameters: df -> DataFrame, column -> String
        Returns: list
        """
        return list(df[column].value_counts().index)

    def get_cpu_guid(series, list):
        """
        """
        hwcpu_match = series.loc[series['guid'].isin(list)]
        hwcpu_match = hwcpu_match[['guid', 'load_ts', 'mean']]
        hwcpu_match['utilization_mean'] = hwcpu_match['mean']
        hwcpu_match = hwcpu_match.drop(columns='mean')
        return hwcpu_match

    def get_temp_guid(series, list):
        """
        """
        hwtemp_match = series.loc[series['guid'].isin(list)]
        hwtemp_match = hwtemp_match[['guid', 'load_ts', 'mean']]
        hwtemp_match['temp_mean'] = hwtemp_match['mean']
        hwtemp_match = hwtemp_match.drop(columns='mean')
        return hwtemp_match

    def get_model_scores(column1, column2):
        """
        Description: returns a dataframe consisting of the accuracy scores of each model
        Parameters: column1 -> Series Object, column2 -> Series Object
        Returns: DataFrame
        """
        df = pd.DataFrame()
        df['name'] = column1
        df['score'] = column2
        return df

    def plot_graphical_model_scores(df):
        """
        Description: returns a saved image of a barplot conveying our accuracy scores
        Parameters: df -> DataFrame
        Returns: Model_scores.png -> file saved in /data/out/
        """
        sns.set(style="whitegrid")
        ax = sns.barplot(y="name", x="score", data=df)
        return plt.savefig("data/out/Model_scores.png")
