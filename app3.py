# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 22:22:40 2022

@author: Administrator
"""

import os
os.getcwd()
os.chdir(r"C:\Users\Administrator\Desktop\PYTHON\Niles")

import numpy as np
import pickle
from flask import Flask, render_template, request

model=pickle.load(open("gbr_model.pkl","rb"))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    x=[float(i) for i in request.form.values()]
    f1=[np.array(x)]
    prediction=model.predict(f1)
    output=prediction[0]
    return render_template('home.html',prediction_text='E20 is {}'.format(output))

if __name__=='__main__':
    app.run(debug=True)