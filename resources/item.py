from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    #Specify all the arguments  
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be left blank!")
    parser.add_argument('store_id', type=int, required=True, help="This field cannot be left blank!")

    @jwt_required() #jwt decorator
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'item not found'},404
    
    
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message":f"item: {name} already exist"}
       
        #catch the arguments 
        data = Item.parser.parse_args()
       
        # **data -> arguments in order
        try:
            item = ItemModel(name, **data)
            item.save_to_db()
        except:
            return {"message":"An error ocurred"},500

        return item.json(), 201 
    
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return ({"Message":"Item deleted!"})


    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        
        if item is None:
            try:
                item = ItemModel(name,**data)
            except:
                return{"mesagge":"An error ocurred"},500
        else:
            try:
                updated_item.update()
            except:
                item.price = ['price']
        item.save_to_db()
        return updated_item.json()
    
class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}