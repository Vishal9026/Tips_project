from flask import Flask, request, app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd


application = Flask(__name__)
app=application

model = pickle.load(open("Model/modelForPrediction.pkl", "rb"))

## Route for homepage

@app.route('/')
def index():
    return render_template('index.html')

## Route for Single data point prediction
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    result=""

    if request.method=='POST':

        total_bill=float(request.form.get("total_bill"))
        tip = float(request.form.get('tip'))
        sex = int(request.form.get('sex'))
        smoker = int(request.form.get('smoker'))
        day = int(request.form.get('day'))
        size = float(request.form.get('size'))

        new_data=scaler.transform([[total_bill,tip,sex,smoker,day,size]])
        predict=model.predict(new_data)
       
        if predict[0] ==1 :
            result = 'Dinner'
        else:
            result ='Lunch'
            
        return render_template('single_prediction.html',result=result)

    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")