from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
# import pandas as pd
from search import search

# Flask App stuff
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/response', methods=['POST'])
@cross_origin()
def response():
    lookup= request.form.get("lookup")
    result  = search(lookup,5)
    # return result
    return render_template('res.html',result=result,lookup=lookup)