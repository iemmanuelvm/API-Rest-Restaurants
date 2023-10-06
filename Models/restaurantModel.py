from db import db
import uuid

# Restaurant Model
class RestaurantModel(db.Model):
    __tablename__ = "restaurant"
    id          = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()), unique=True)
    rating      = db.Column(db.Integer, nullable=False)
    name        = db.Column(db.String, nullable=False)
    site        = db.Column(db.String, nullable=False)
    email       = db.Column(db.String, nullable=False)
    phone       = db.Column(db.String, nullable=False)
    street      = db.Column(db.String, nullable=False)
    city        = db.Column(db.String, nullable=False)
    state       = db.Column(db.String, nullable=False)
    lat         = db.Column(db.Float(precision=10), nullable=False)
    lng         = db.Column(db.Float(precision=10), nullable=False)