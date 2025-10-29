from flask import Blueprint
from flask import render_template , request , current_app , session , redirect , url_for
from models import  Department
from config import db
from datetime import time


department_bp = Blueprint( 'department'  , __name__ , template_folder='Templates' , static_folder='Static' , url_prefix='/department')


@department_bp.route('/<name>')
def dashboard(name):
    department = Department.query.filter(Department.name == name).first() 
    doctors = department.doctors

    return render_template('department.html' , department=department , doctors = doctors)


@department_bp.route('/<doctor_name>/appointments')
def handle_appointments(doctor_name):
    sample = [ 
            ('24-10-2025' ,  [   ( [ time(10,12)  , time(11 , 12) ]  , None  )    ]  ) ,   
            ('25-10-2025', []), 
            ('26-10-2025', []), 
            ('27-10-2025', []), 
            ('28-10-2025', []), 
            ('29-10-2025', []), 
            ('30-10-2025', []), 
            ('31-10-2025', []), 
            ('01-11-2025', []),  # Date rolls over from October to November
            ('02-11-2025', []), 
            ('03-11-2025', [])
        ]   
    
    
    return render_template('appointment_system.html' , days =sample)