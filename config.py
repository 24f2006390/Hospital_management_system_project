
from flask_sqlalchemy import SQLAlchemy 
db  = SQLAlchemy()
class config :
    SQLALCHEMY_DATABASE_URI = 'sqlite:///hospital.db'
    SECRET_KEY = 'MY_KEY_SUPER_SECRET123'
    