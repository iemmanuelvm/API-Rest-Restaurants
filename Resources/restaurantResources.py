from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

import csv, os

from db import db
from Models import RestaurantModel
from Schemas import RestaurantSchema, RestaurantUpdateSchema

blp = Blueprint("Restaurants", "restaurants", description="Operations on restaurants")

@blp.route("/restaurants")
class RestaurantList(MethodView):
    @blp.response(200, RestaurantSchema(many=True))
    def get(self):
        return RestaurantModel.query.all()
    @blp.arguments(RestaurantSchema)
    @blp.response(201, RestaurantSchema)
    def post(self, restaurant_data):
        restaurant = RestaurantModel(**restaurant_data)
        try:
            db.session.add(restaurant)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A restaurant with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the restaurant.")

        return restaurant

@blp.route("/restaurants/<string:restaurant_id>")
class Restaurant(MethodView):
    @blp.response(200, RestaurantSchema)
    def get(self, restaurant_id):
        store = RestaurantModel.query.get_or_404(restaurant_id)
        return store

    def delete(self, restaurant_id):
        store = RestaurantModel.query.get_or_404(restaurant_id)
        db.session.delete(store)
        db.session.commit()
        return {"message": "Restaurant deleted"}, 200
    
    @blp.arguments(RestaurantUpdateSchema)
    @blp.response(200, RestaurantUpdateSchema)
    def put(self, item_data, restaurant_id):
        item = RestaurantModel.query.get(restaurant_id)

        if item:
            item.rating     = item_data["rating"]
            item.name       = item_data["name"]
            item.site       = item_data["site"]
            item.email      = item_data["email"]
            item.phone      = item_data["phone"]
            item.street     = item_data["street"]
            item.city       = item_data["city"]
            item.state      = item_data["state"]
            item.lat        = item_data["lat"]
            item.nalngme    = item_data["lng"]

        else:
            item = RestaurantModel(id=restaurant_id, **item_data)

        db.session.add(item)
        db.session.commit()

        return item
    
# Define a new route to seed data from CSV
@blp.route('/restaurants/seed-data')
class Restaurant(MethodView):
    # @blp.response(200, RestaurantSchema)
    def post(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        data_file_path = os.path.join(script_directory, '..', 'Data', 'restaurantes.csv')

        try:
            with open(data_file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    restaurant = RestaurantModel(
                        id=row['id'],
                        rating=int(row['rating']),
                        name=row['name'],
                        site=row['site'],
                        email=row['email'],
                        phone=row['phone'],
                        street=row['street'],
                        city=row['city'],
                        state=row['state'],
                        lat=float(row['lat']),
                        lng=float(row['lng'])
                    )
                    # print(restaurant.city)
                    db.session.add(restaurant)
                    db.session.commit()
        
        except IntegrityError:
            abort(
                400,
                message="A restaurant with that restaurant already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the restaurant.")
        
        return {"message": "SEED EXECUTED"}, 200
    