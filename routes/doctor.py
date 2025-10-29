
from flask import Blueprint
from flask import render_template , request , current_app , session , redirect , url_for
from models import Doctor , Department , Doctor_availability
from config import db
from datetime import datetime , timedelta


doctor_bp = Blueprint( 'doctor'  , __name__ , template_folder='Templates' , static_folder='Static' , url_prefix='/doctor')

@doctor_bp.route('/dashboard')
def dashboard():
    user_name = session.get('doctor_user_name')
    if user_name is None  : 
        return "Not allowed to view dashboard" , 401
    doctor = Doctor.query.filter( Doctor.user_name == user_name).first() 
    if doctor == None:
        return "NO such Docotor"  , 404 

    
    current_app.logger.info(user_name)
    departments = Department.query.all()

    
    next_days= 7 ; 
    today_date = datetime.now()
    availability = { }
    for day in range( 1 , next_days+1) : 

        current_date =today_date + timedelta(days=day)  

        availability[current_date.date().__str__()] = [ ]; 
        for slot_no in range(1 ,3) : 
            slot = Doctor_availability.query.filter( Doctor_availability.doctor_id == doctor.id , 
                                            Doctor_availability.date == current_date.date() ,
                                            Doctor_availability.slot_no == slot_no).first() # seconds to ms

            if slot != None : 
                availability[current_date.date().__str__()].append(slot_no)




    return render_template('doctor_dash.html' , availability = availability  ,user_name = user_name , departments=departments )



@doctor_bp.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method =='GET' : 
        if session.get('doctor_user_name') :
            return redirect('dashboard') 
        return render_template('doctor_login.html')
    data = request.get_json() 
    user_name = data.get('doctor_user_name') 
    
    doctor = Doctor.query.filter( Doctor.user_name == user_name).first() 
    if doctor == None : 
        return "No such user" , 404 
    
    session['doctor_user_name'] = user_name ; 
    return redirect('dashboard') 
    


@doctor_bp.route('/appointment')
def handle_appointment():
    
    return render_template('/appointment_doctor.html')

@doctor_bp.route('/book/<date>/<int:slot_no>')
def book(date , slot_no):
    user_name = session.get('doctor_user_name')
    if user_name is None : 
        return "Not allowed to view dashboard" , 401
    
    date =  datetime.strptime(date , '%Y-%m-%d')
    doctor = Doctor.query.filter( Doctor.user_name == user_name).first() 

    if Doctor_availability.query.filter( Doctor_availability.doctor_id == doctor.id ,
                                         Doctor_availability.date == date , Doctor_availability.slot_no== slot_no).first() == None :
        db.session.add( Doctor_availability(doctor_id = doctor.id , date= date , slot_no= slot_no) )
        db.session.commit() 
    
    return "Booked " , 200 


