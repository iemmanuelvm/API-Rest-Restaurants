from marshmallow import Schema, fields

# Restaurant Schema
class RestaurantSchema(Schema):
    id      = fields.UUID(dump_only=True, required=True)
    rating  = fields.Int(required=True)
    name    = fields.Str(required=True)
    site    = fields.Str(required=True)
    email   = fields.Email(required=True)
    phone   = fields.Str(required=True)
    street  = fields.Str(required=True)
    city    = fields.Str(required=True)
    state   = fields.Str(required=True)
    lat     = fields.Float(required=True)
    lng     = fields.Float(required=True)

class RestaurantUpdateSchema(Schema):
    name    = fields.Str()
    rating  = fields.Int()
    name    = fields.Str()
    site    = fields.Str()
    email   = fields.Email()
    phone   = fields.Str()
    street  = fields.Str()
    city    = fields.Str()
    state   = fields.Str()
    lat     = fields.Float()
    lng     = fields.Float()