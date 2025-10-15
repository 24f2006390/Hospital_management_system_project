from flask import Blueprint
from flask import render_template


patient_bp = Blueprint( 'patient'  , __name__ , template_folder='Templates' , static_folder='Static')

@patient_bp.route('/patient/dashboard')
def dashboard():
    print("hello")
    return render_template('patient_dash.html')




