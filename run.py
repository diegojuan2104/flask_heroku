from app import app
from db import db

db.init_app(app)

@app.before_first_request #To Create all the tables before run 
def create_tables():
    db.create_all()