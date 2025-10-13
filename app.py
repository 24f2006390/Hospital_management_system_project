from flask import Flask 
from config import config , db
import models.model
app= Flask(__name__)

def create_app():
    app.config.from_object(config)
    db.init_app( app) 
    db.create_all()

print("Hello")
if __name__ == '__main__':
    print("App Started")
    with app.app_context():
        create_app() 
    app.run(debug=True) 

