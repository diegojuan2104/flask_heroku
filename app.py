from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store,StoreList

app = Flask(__name__) #This means that this it's the main doc where flask runs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # To locate the db doc, and add sqlite,postgreSQL,Oracle whatever....
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app) #Allow add Resources from flask Rest-full
app.secret_key = '123456789123456789qwewqqwer'

@app.before_first_request #To Create all the tables before run 
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # using URL/auth whit authenticate comfirm the user and password, and with identity returns the user token encripted 

#Add all the resources 
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister,'/register')
api.add_resource(StoreList,'/stores')
api.add_resource(Store,'/store/<string:name>')

# Allows only run in app.py
if __name__ == '__main__':
    from db import db 
    db.init_app(app)
    app.run(port = 3000, debug=True)