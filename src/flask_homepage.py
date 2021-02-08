"""
Jon Zhang, Keshan Chen, Vince Wong
flask_homepage.py
"""
from flask import Flask
import os
app = Flask(__name__)

### TO BE EXPANDED ON GREATLY

@app.route("/")
def home():
    return "Predicting a user’s persona based on their average CPU utilization and core temperature"

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4444)))
