from . import ma
from marshmallow import fields


class CustomerSchema(ma.Schema):
    id = fields.Integer(required=False) #Primary Key is Autogenerated and doesn't need to be apart of the payload
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    role_id = fields.String(required=True)

    class Meta: 
        fields = ("id", "name", "email", "phone", "username", "password", "role_id")

    
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True, exclude=["password"])

class CustomerOrderSchema(ma.Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)

class CustomerOrderSchema(ma.Schema):
    id = fields.Integer(required=False) #Primary Key is Autogenerated and doesn't need to be apart of the payload
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    orders = fields.Nested("OrderSchema", many=True)

    class Meta: 
        fields = ("id", "name", "email", "phone", "username", "password")


class CustomerCart(ma.Schema):
    name = fields.String(required=True)
    cart = fields.Nested("ProductSchema", many=True)

    
    class Meta:
        fields = ("name", "cart")

customer_cart = CustomerCart()