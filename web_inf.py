import random
import string
import pandas as pd
from flask import Flask, render_template, url_for
from flask import jsonify
import os
from flask import request,redirect
from flask_cors import CORS
from werkzeug.utils import secure_filename
from flask import send_from_directory
app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['*'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):

    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    """
    return True


@app.route('/')
def hello_world():
    # return 'Hello, World!'
    return render_template('home.html')


@app.route('/data-analyst/upload-file',methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            data = pd.read_csv(file)
            print(data)
            size = random.randint(8, 15)
            filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            resp = jsonify(filename=filename, success=True)

            return resp
            # return redirect(url_for('uploaded_file',filename=filename))
    return 'testing'


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/fake4a')
def fake4a():
    arg1 = request.values.get('service')
    if arg1 is None:
        return 'need service as parameter !'
    # print(arg1)
    return redirect(arg1+'?ticket=A123B456C789')


if __name__ == '__main__':
    print("start...")
    app.run(host='0.0.0.0', port=5000)
