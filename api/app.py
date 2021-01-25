from flask_ngrok import run_with_ngrok
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/'
ALLOWED_EXTENSIONS = {'h5ad', 'txt'}


app = Flask(__name__)
run_with_ngrok(app)   #starts ngrok when the app is run
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            local_file = open("data.h5ad", "wb")
            local_file.write(file.read())
            local_file.close()
            return redirect(url_for('run_model'))
            
    return '''
          <!doctype html>
          <title>Upload new an anndata file with a .h5ad extension</title>
          <h1>Upload data</h1>
          <form method=post enctype=multipart/form-data>
            <input type=file name=file>
            <input type=submit value=Upload>
          </form>
          '''