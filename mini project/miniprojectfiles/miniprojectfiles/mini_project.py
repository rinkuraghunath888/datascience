from flask import Flask, render_template,request

import requests
import pickle
import numpy as np
import sklearn
import pandas
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
#model = pickle.load(open('tyre_quality.pkl','rb'))
with open('tyre_quality.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/',methods=['GET'])
def home():
    return render_template('finalminipro_2.html')
standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Section_width =float(request.form['Section_width'])
        Width_tread =float(request.form['Width_tread'])
        Outer_diameter =float(request.form['Outer_diameter'])
        Machine_Speed =int(request.form['Machine_Speed'])
        
        prediction=model.predict(np.array([Section_width,Width_tread,Outer_diameter,Machine_Speed]).reshape(1,-1))
        output=round(prediction[0],2)
        if output<0:
            return render_template('finalminipro_2.html',prediction_texts="Oops! Do you want to check the input values?")
        else:
            return render_template('finalminipro_2.html',prediction_text="Predicted Performance Rating: {} ".format(output))
    else:
        return render_template('finalminipro_2.html')

if __name__=="__main__":
    #app.run(debug=True,use_reloader=False)
    app.run()