from flask import Blueprint , render_template , request
from flask import current_app 
from models import Department , Doctor , Patient
from config import db
admin_bp = Blueprint('admin' , __name__ , template_folder='Templates' , 
                     static_folder='Static' , url_prefix='/admin')


@admin_bp.route('/dashboard')
def dashboard():
    current_app.logger.info("Admin accessed dashboard")
    departments = Department.query.all()
    doctors = Doctor.query.all() 
    patients = Patient.query.all() 
    return render_template('admin.html' , departments = departments , doctors=doctors , patients = patients)

@admin_bp.route('/add/department' , methods=['GET' , 'POST'])
def add_depart():
    if request.method == 'GET' : 
        return render_template('add_depart.html')
    current_app.logger.info("Post request sent to add department route")
    data  = request.get_json() ; 
    current_app.logger.info(data)
    name = data.get('name') ; 
    description = data.get('description') 
    email = data.get('email')
    depart = Department(name=name , description = description , email_id = email) ; 
    db.session.add( depart) ; 
    db.session.commit()
    return '' , 200 

@admin_bp.route('/add/doctor' , methods=['GET' , 'POST'])
def add_doctor():
    if request.method == 'GET' : 
        return render_template('add_doctor.html')
    current_app.logger.info("Post request sent to add doctor route")
    data  = request.get_json() ; 
    current_app.logger.info(data)

    user_name= data.get('user_name')
    first_name = data.get('first_name') ; 
    last_name = data.get('last_name') 
    d_name = data.get('department')
    department  = Department.query.filter( Department.name == d_name).first() 

    if department is None : 
        return "NO such department"  ,404 

    doctor = Doctor( user_name=user_name ,first_name=first_name , last_name = last_name , department_id= department.id ) ; 
    
    db.session.add( doctor) ; 
    db.session.commit()
    return '' , 200 
