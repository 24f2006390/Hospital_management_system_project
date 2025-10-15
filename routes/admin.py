from flask import Blueprint , render_template , request
from flask import current_app 
from models import Department
from config import db
admin_bp = Blueprint('admin' , __name__ , template_folder='Templates' , 
                     static_folder='Static' , url_prefix='/admin')


@admin_bp.route('/dashboard')
def dashboard():
    current_app.logger.info("Admin accessed dashboard")
    departments = Department.query.all()
    return render_template('admin.html' , departments = departments)

@admin_bp.route('/add/department' , methods=['GET' , 'POST'])
def add_depart():
    if request.method == 'GET' : 
        return render_template('add_depart.html')
    current_app.logger.info("Post request sent to add department route")
    data  = request.get_json() ; 
    current_app.logger.info(data)
    name = data.get('name') ; 
    description = data.get('name') 
    email = data.get('email')
    depart = Department(name=name , description = description , contact_email = email) ; 
    db.session.add( depart) ; 
    db.session.commit()
    return '' , 200 
    
