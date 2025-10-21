from flask import Blueprint
from flask import render_template , request , current_app , session , redirect , url_for
from models import  Department
from config import db



department_bp = Blueprint( 'department'  , __name__ , template_folder='Templates' , static_folder='Static' , url_prefix='/department')


@department_bp.route('/<name>')
def dashboard(name):
    department = Department.query.filter(Department.name == name).first() 
    doctors = department.doctors

    return render_template('department.html' , department=department , doctors = doctors)

