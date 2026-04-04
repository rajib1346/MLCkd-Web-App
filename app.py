import pandas as pd
import numpy as np
from flask import Flask, request, render_template
import pickle
import time

#Create an app object using the Flask class. 
app = Flask(__name__)

#Load the trained model. (Pickle file)
model = pickle.load(open('models/model.pkl', 'rb'))

#Define the route to be home. 
#The decorator below links the relative route of the URL to the function it is decorating.
#Here, home function is with '/', our root directory. 
#Running the app sends us to index.html.
#Note that render_template means it looks for the file in the templates folder. 

#use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def home():
    return render_template('index.html')

#You can use the methods argument of the route() decorator to handle different HTTP methods.
#GET: A GET message is send, and the server returns data
#POST: Used to send HTML form data to the server.
#Add Post method to the decorator to allow for form submission. 
#Redirect to /predict page with the output
@app.route('/predict',methods=['post'])
def predict():
    
    # Get user input from the form
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

    start_time = time.time()
    prediction = model.predict([[age,bp,sg,al,su,bgr,bu,sc,sod,pot,hemo,rbc,pc,pcc,ba,wc,htn,dm,cad,appet,pe,ane]])  
    end_time = time.time()
    testing_time = end_time - start_time
    
    if rbc == 0:
        rbc = "Abnormal"
    else:
        rbc = "Normal"
        
    if pc == 0:
        pc = "Abnormal"
    else:
        pc = "Normal"  
        
    if pcc == 0:
        pcc = "Abnormal"
    else:
        pcc = "Normal"  
        
    if ba == 0:
        ba = "Not Present"
    else:
        ba = "Present"  

    if htn == 0:
        htn = "No"
    else:
        htn = "Yes"          
        
    if dm == 0:
        dm = "No"
    else:
        dm = "Yes"         

    if cad == 0:
        cad = "No"
    else:
        cad = "Yes"   

    if appet == 0:
        appet = "Good"
    else:
        appet = "Poor"          
 
    if pe == 0:
        pe = "No"
    else:
        pe = "Yes" 
        
    if ane == 0:
        ane = "No"
    else:
        ane = "Yes"        
        
        
    if prediction == 0:
        result = "No Kidney Disease"
        color = 'green'
        status = 'Kidney Disease Negative'
    else:
        result = "Kidney Disease"
        color = 'red'
        status = 'Kidney Disease Positive'

    return render_template('result.html', name=name, bg=bg, sex=sex, age=age,bp=bp, result=result, color=color, status=status, sg=sg,al=al,su=su,bgr=bgr,bu=bu,sc=sc,sod=sod,pot=pot,hemo=hemo,rbc=rbc,pc=pc,pcc=pcc,ba=ba,wc=wc,htn=htn,dm=dm,cad=cad,appet=appet,pe=pe,ane=ane,  testing_time=  testing_time)



#When the Python interpreter reads a source file, it first defines a few special variables. 
#For now, we care about the __name__ variable.
#If we execute our code in the main program, like in our case here, it assigns
# __main__ as the name (__name__). 
#So if we want to run our code right here, we can check if __name__ == __main__
#if so, execute it here. 
#If we import this file (module) to another file then __name__ == app (which is the name of this python file).

if __name__ == "__main__":
    app.run()
