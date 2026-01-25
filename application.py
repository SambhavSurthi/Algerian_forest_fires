import pickle
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from flask import Flask,render_template,request,jsonify
application = Flask(__name__)
app=application

#models
liModel=pickle.load(open('models/linear_regression.pkl','rb'))
rModel=pickle.load(open('models/ridge_regression.pkl','rb'))
lModel=pickle.load(open('models/lasso_regression.pkl','rb'))
eModel=pickle.load(open('models/elasticnet_regression.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def prediction():
    if request.method=='POST':
        input_data = {
            'day': float(request.form['day']),
            'month': float(request.form['month']),
            'year': float(request.form['year']),
            'Temperature': float(request.form['Temperature']),
            'RH': float(request.form['RH']),
            'Ws': float(request.form['Ws']),
            'Rain': float(request.form['Rain']),
            'FFMC': float(request.form['FFMC']),
            'DMC': float(request.form['DMC']),
            'DC': float(request.form['DC']),
            'ISI': float(request.form['ISI']),
            'BUI': float(request.form['BUI'])
        }

        

        input_df = pd.DataFrame([input_data])

        liprediction = liModel.predict(input_df)
        rprediction = rModel.predict(input_df)
        lprediction = lModel.predict(input_df)
        eprediction = eModel.predict(input_df)

        results={
            'Linear Regression Model':liprediction,
            'Ridge Regression Model':rprediction,
            'Lasso Regression Model':lprediction,
            'ElasticNet Regression Model':eprediction
        }

        return render_template('prediction.html',results=results)
    else:
        return render_template('prediction.html')

@app.route('/eda')
def eda():
    return render_template('EDA_report.html')

if __name__ == '__main__':
    app.run()