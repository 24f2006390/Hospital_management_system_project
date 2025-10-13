
from 
from flask import render_template



@app.route('/patient/dashboard')
def dashboard():
    print("hello")
    return render_template('Templates/patient.py')




