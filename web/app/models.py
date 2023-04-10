
import sqlalchemy as sa
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin



from app import db, app

class Worker(db.Model, UserMixin):  
    __tablename__ = 'workers'

    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(40), nullable=False)
    login = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    
    def check_password(self, password: str):
        return self.password == password
    

class Event(db.Model, UserMixin):  
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)    
    year = db.Column(db.String(40), nullable=False)
    day = db.Column(db.String(250), nullable=False)
    desc = db.Column(db.String(100), nullable=False)
    
    



    



    


