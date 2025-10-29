from flask import Flask 
from config import config , db
from routes import patient_bp ,doctor_bp
from routes import admin_bp  

from routes import home_bp , department_bp
import logging

app= Flask(__name__)

log_file_handler = logging.FileHandler('app.log')

app.logger.handlers.clear()
app.logger.addHandler(log_file_handler)
app.logger.setLevel(logging.DEBUG)

def create_app():
    app.config.from_object(config)
    db.init_app( app) 
    db.create_all()

    # Registering Blueprints
    app.register_blueprint(patient_bp) ; 
    app.register_blueprint(admin_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(department_bp)
    app.register_blueprint(doctor_bp) ; 



if __name__ == '__main__':
    app.logger.info("App Started")
    with app.app_context():
        create_app() 
    app.run(debug=True) 

