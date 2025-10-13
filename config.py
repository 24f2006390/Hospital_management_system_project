
from flask_sqlalchemy import SQLAlchemy 
db  = SQLAlchemy()
class config :
    SQLALCHEMY_DATABASE_URI = 'sqlite:///hospital.db'
    