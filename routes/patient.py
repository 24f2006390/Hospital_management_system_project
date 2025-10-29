from flask import Blueprint
from flask import render_template , request , current_app , session , redirect , url_for
from models import Patient , Department
from config import db



patient_bp = Blueprint( 'patient'  , __name__ , template_folder='Templates' , static_folder='Static' , url_prefix='/patient')

@patient_bp.route('/dashboard')
def dashboard():
    user_name = session.get('user_name')
    if user_name is None : 
        return "Not allowed to view dashboard" , 401
    
    current_app.logger.info(user_name)
    departments = Department.query.all()

    return render_template('patient_dash.html' , user_name = user_name , departments=departments )



@patient_bp.route('/login' , methods=['GET' , 'POST'])
def patient_login():
    if request.method =='GET' : 
        if session.get('user_name') :
            return redirect('dashboard') 
        return render_template('patient_login.html')
    data = request.get_json() 
    user_name = data.get('user_name') 
    
    patient = Patient.query.filter( Patient.user_name == user_name).first() 
    if patient == None : 
        return "No such user" , 404 
    
    session['user_name'] = user_name ; 
    return redirect('dashboard') 
    



@patient_bp.route('/register' , methods=['GET' , 'POST'])
def patient_register():
    if request.method == 'GET' :
        return render_template('patient_register.html')
    current_app.logger.info("Post request sent to Patient register route")
    data  = request.get_json() ;

    current_app.logger.info(data)

    user_name = data.get('user_name')
    first_name = data.get('first_name') ;
    last_name = data.get('last_name')

    patient = Patient(   user_name=user_name ,first_name=first_name , last_name = last_name ) ;
    db.session.add( patient) ;
    db.session.commit()
    return '' , 200