"""
Jon Zhang, Keshan Chen, Vince Wong
flask_homepage.py
"""
import pandas as pd
from flask import Flask, jsonify, request, render_template
import pickle
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
from flask import Flask
import os
app = Flask(__name__)

### TO BE EXPANDED ON GREATLY
df = pd.read_csv('../data/raw/test180.csv')

Y = df['persona']
X = df.drop(columns=['persona'])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = DecisionTreeClassifier(max_depth=5)
model.fit(X, Y)
model.score(X, Y)

pickle.dump(model, open('model.pkl', 'wb'))
model = pickle.load(open('model.pkl','rb'))

@app.route("/", methods=['GET', 'POST'])     
def home():
    return "Predicting a user’s persona based on their average CPU utilization and core temperature"

def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': int(result[0])}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4444)))
