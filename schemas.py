from marshmallow import Schema, fields

class UsersBaseSchema(Schema): 
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)  
    email = fields.Email()
    phone_number = fields.Str(required=True) 
    password = fields.Str(required=True) 
    account = fields.Str(required=True) 
    token = fields.Str(required=True) 

class BpnBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    phone_number = fields.Str(required=True) 

class ActionsBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    stage = fields.Int(dump_only=True)
    kind = fields.Int(dump_only=True)
    key_number = fields.Int(dump_only=True)
    paramaters = fields.Str(required=True)

class CalendarBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    taken_date = fields.Date().required()