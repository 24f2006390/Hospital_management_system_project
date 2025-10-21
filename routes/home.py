from flask import Blueprint
from flask import render_template , request , current_app
from models import Patient 
from config import db


home_bp = Blueprint( 'home'  , __name__ , template_folder='Templates' , static_folder='Static' )

@home_bp.route('/')
def dashboard():
    return render_template('home.html')



