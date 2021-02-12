"""
Jon Zhang, Keshan Chen, Vince Wong
run.py
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

# my edit
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification

sys.path.insert(0, 'src')
from src.data_exploration import *

def main(targets):
    """
    this method will run all the methods within class data_exploration.py
    """
    # Parse through the datasets and select only relevant columns
    cpu_df = data_exploration.parse_cpu_data("data/raw/hw_metric_histo.csv000")
    sys_df = data_exploration.parse_sys_data("data/raw/system_sysinfo_unique_normalized.csv000")

    # Create a new reference to the optimized DataFrame
    optimized_df = data_exploration.optimize_dataframe(cpu_df)

    # grab the specific column "HW::CORE:C0:PERCENT" as a feature
    cpu = data_exploration.get_stats(optimized_df, "name", "HW::CORE:C0:PERCENT:")

    # grab the specific column "HW::CORE:TEMPERATURE:CENTIGRADE" as a feature
    temp = data_exploration.get_stats(optimized_df, "name", "HW::CORE:TEMPERATURE:CENTIGRADE:")

    # grab the GUIDs from each dataset and put them into lists
    sys_guid = data_exploration.get_guid(sys_df, 'guid')
    hw_guid = data_exploration.get_guid(cpu_df, 'guid')

    # checking for the GUID overlap in both datasets
    syshw_overlap = [guid for guid in sys_guid if guid in hw_guid]

    # objective is to create a dataframe of only matching GUIDs
    hwcpu_match = data_exploration.get_cpu_guid(cpu, syshw_overlap)

    # only grabbing the relevant columns to be matched on
    hwtemp_match = data_exploration.get_temp_guid(temp, syshw_overlap)

    # instantiating our dataframes to be joined
    hwtemp = pd.DataFrame(hwtemp_match.groupby('guid')['temp_mean'].mean())
    hwcpu = pd.DataFrame(hwcpu_match.groupby('guid')['utilization_mean'].mean())

    # joining our matched dataframes together, only using relevant columns
    combined = sys_df.join(hwcpu, on=['guid'], how='left')
    combined = combined.join(hwtemp, on=['guid'], how='left')
    combined = combined.drop(columns=['guid', 'model_normalized', "processornumber"])

    # create copy of our joined dataframe to be used for modelling
    feature_columns = combined.copy()

    # selecting only relevant columns to use for features
    feature_columns = feature_columns[['os','cpu_family', 'cpuvendor',
                                       'graphicscardclass', 'persona']]

    # creating a completely one-hot encoded dataframe only containing relevant columns
    dummy = pd.get_dummies(feature_columns)

    # converting our categorical variables to be predicted on into numerical values
    cleanup_nums = {'persona': {'Web User': 0, 'Casual User': 1, 'Gamer':2, 'Casual Gamer': 3,
                                'Office/Productivity':4, 'Content Creator/IT': 5,
                                'Communication': 6, 'Win Store App User': 7, 'Entertainment': 8,
                                'File & Network Sharer':9, 'Unknown': 10}}

    # replacing the values in the column 'persona' to be numerical
    encode_persona = combined['persona'].to_frame().replace(cleanup_nums)

    # putting our old means back into the dummy dataframe
    dummy['util_mean'] = combined['utilization_mean']
    dummy['temp_mean'] = combined['temp_mean']
    # dummy = dummy.drop(columns=['persona'])
    dummy['persona'] = encode_persona['persona']

    dummy = dummy.dropna()
    nona_test = dummy.copy()

    # we want to predict on Y
    Y = nona_test['persona']
    X = nona_test.drop(columns=['persona'])

    # creating our test/train split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    # all the models we are going to use
    names = ["Nearest_Neighbors", "Linear_SVM", "Polynomial_SVM", "RBF_SVM", "Gradient_Boosting"]

    # all of our predictors scaled to the degree of our datasets
    classifiers = [KNeighborsClassifier(3),
                   SVC(kernel="linear", C=0.025),
                   SVC(kernel="poly", degree=3, C=0.025),
                   SVC(kernel="rbf", C=1, gamma=2),
                   GradientBoostingClassifier(n_estimators=100, learning_rate=1.0)]

    scores = []
    # we write in our accuracy scores to [scores]
    for name, clf in zip(names, classifiers):
        clf.fit(X_train, Y_train)
        score = clf.score(X_test, Y_test)
        scores.append(score)

    show = data_exploration.get_model_scores(names, scores)
    model_scores = data_exploration.plot_graphical_model_scores(show)

if __name__ == "__main__":
    targets = sys.argv[1:]
    main(targets)
