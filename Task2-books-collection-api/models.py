from marshmallow import Schema, fields, validate, ValidationError

class BookSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1, max=100))
    author = fields.String(required=True, validate=validate.Length(min=1, max=100))
    isbn = fields.String(required=True, validate=validate.Length(equal=13))
    published_year = fields.Integer(required=True, validate=lambda x: 1000 <= x <= 9999)

def validate_book(data):
    schema = BookSchema()
    return schema.load(data)