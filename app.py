import pandas as pd
import numpy as np
from flask import Flask, request, render_template
import time
from joblib import load   # better than pickle

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = load('models/model.joblib')   # make sure file exists

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input
        name = request.form['name']
        bg = request.form['bg']
        sex = request.form['sex']

        age = float(request.form['age'])
        bp = float(request.form['bp'])
        sg = float(request.form['sg'])
        al = float(request.form['al'])
        su = float(request.form['su'])
        bgr = float(request.form['bgr'])
        bu = float(request.form['bu'])
        sc = float(request.form['sc'])
        sod = float(request.form['sod'])
        pot = float(request.form['pot'])
        hemo = float(request.form['hemo'])
        rbc = float(request.form['rbc'])
        pc = float(request.form['pc'])
        pcc = float(request.form['pcc'])
        ba = float(request.form['ba'])
        wc = float(request.form['wc'])
        htn = float(request.form['htn'])
        dm = float(request.form['dm'])
        cad = float(request.form['cad'])
        appet = float(request.form['appet'])
        pe = float(request.form['pe'])
        ane = float(request.form['ane'])

        # Prepare input for model
        features = [[age, bp, sg, al, su, bgr, bu, sc, sod, pot,
                     hemo, rbc, pc, pcc, ba, wc, htn, dm, cad, appet, pe, ane]]

        # Prediction
        start_time = time.time()
        prediction = model.predict(features)
        end_time = time.time()
        testing_time = round(end_time - start_time, 4)

        # Convert numeric to readable
        rbc = "Normal" if rbc == 1 else "Abnormal"
        pc = "Normal" if pc == 1 else "Abnormal"
        pcc = "Present" if pcc == 1 else "Not Present"
        ba = "Present" if ba == 1 else "Not Present"
        htn = "Yes" if htn == 1 else "No"
        dm = "Yes" if dm == 1 else "No"
        cad = "Yes" if cad == 1 else "No"
        appet = "Good" if appet == 1 else "Poor"
        pe = "Yes" if pe == 1 else "No"
        ane = "Yes" if ane == 1 else "No"

        # Result
        if prediction[0] == 0:
            result = "No Kidney Disease"
            color = "green"
            status = "Kidney Disease Negative"
        else:
            result = "Kidney Disease"
            color = "red"
            status = "Kidney Disease Positive"

        return render_template(
            'result.html',
            name=name, bg=bg, sex=sex, age=age, bp=bp,
            result=result, color=color, status=status,
            sg=sg, al=al, su=su, bgr=bgr, bu=bu, sc=sc,
            sod=sod, pot=pot, hemo=hemo, rbc=rbc, pc=pc,
            pcc=pcc, ba=ba, wc=wc, htn=htn, dm=dm, cad=cad,
            appet=appet, pe=pe, ane=ane,
            testing_time=testing_time
        )

    except Exception as e:
        return f"Error: {str(e)}"


# Run app
if __name__ == "__main__":
    app.run(debug=True)
