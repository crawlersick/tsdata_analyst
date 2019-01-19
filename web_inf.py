
from flask import Flask,render_template,url_for
from flask import jsonify
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return render_template('home.html')

if __name__ == '__main__':
    print("start...")
    app.run(host='0.0.0.0',port=5000)
