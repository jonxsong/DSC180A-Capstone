from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def home():
    return "How Does Your Connected Devices Affect Your Battery Life?"

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))
