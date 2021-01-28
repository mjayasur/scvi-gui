from flask_ngrok import run_with_ngrok
import os
from flask import Flask, flash, request, redirect, url_for, jsonify, render_template
from werkzeug.utils import secure_filename
import json

import scanpy as sc
import scvi
UPLOAD_FOLDER = '/'
ALLOWED_EXTENSIONS = {'h5ad', 'txt'}


app = Flask(__name__, static_folder='static')
run_with_ngrok(app)   #starts ngrok when the app is run
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'GET':
        return render_template("upload.html")

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
            return redirect("/setup_anndata")
    

@app.route('/setup_anndata', methods=['GET', 'POST'])
def setup_anndata():
    if request.method == 'GET':
        adata = scvi.data.read_h5ad("data.h5ad")
        return render_template("setup_anndata.html", 
            batch_keys = [None] + list(adata.obs.keys()), 
            obsm_keys = [None] + list(adata.obsm.keys()),
            uns_keys = [None] + list(adata.uns.overloaded.keys()),
            )
    if request.method == 'POST':
        print ("from anndata", request.form)
        config = {
            'batch_key' : request.form['batch_key'],
            'protein_expression_obsm_key' : request.form['protein_expression_obsm_key'],
            'protein_names_uns_key' : request.form['protein_names_uns_key'],
        }
        with open('anndata_config.json', 'w') as fp:
            json.dump(config, fp)
        return redirect('/train_model')

@app.route('/train_model', methods=['GET', 'POST'])
def train_model():
    if request.method == 'GET':
        return render_template("/train_model.html")
    if request.method == 'POST':
        
        anndata_config =  json.load(open("anndata_config.json", 'r'))
        anndata_config = {key : anndata_config[key] for key in anndata_config  if anndata_config[key] and anndata_config[key] != 'None'}
        print ("anndata_config", anndata_config)
        # print (request.form)
        model_params = request.form.to_dict(flat=False)

        adata = scvi.data.read_h5ad("data.h5ad")
        sc.pp.filter_genes(adata, min_counts=3)

        sc.pp.highly_variable_genes(
            adata,
            n_top_genes=2000,
            subset=True,
            flavor="seurat_v3"
        )

        scvi.data.setup_anndata(
            adata, 
            **anndata_config
        )

        model = scvi.model.SCVI(adata)

        model.train()

        model.save("my_model")

        return redirect('/')

@app.route('/viz_results', methods=['GET', 'POST'])
def viz_results():
    if request.method == 'GET':
        return render_template("viz_results")
    
    else:

        return redirect("/viz_results")