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
    stage = fields.Int(required=True)
    kind = fields.Int(required=True)
    key_number = fields.Int(required=True)
    paramaters = fields.Str(required=True)

class CalendarBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    taken_date = fields.Date()
    room_number = fields.Int(required=True)

class BpnSchema(BpnBaseSchema):
    user_id = fields.Int(required=True, load_only = True)
    user = fields.Nested(UsersBaseSchema(), dump_only=True)
    actions = fields.List(fields.Nested(ActionsBaseSchema()), dump_only=True) 
    taken_dates = fields.List(fields.Nested(CalendarBaseSchema()), dump_only=True) 

class UsersSchema(UsersBaseSchema):
    bpn = fields.List(fields.Nested(BpnBaseSchema()), dump_only=True) 
    
class ItemIdSchema(Schema):
    item_id = fields.String(required=True, description="The ID of the item")


class ActionsSchema(ActionsBaseSchema):
    bpn_id = fields.Int(required=True, load_only = True)
    bpn = fields.Nested(BpnBaseSchema(), dump_only=True)

class CalendarSchema(CalendarBaseSchema):
    bpn_id = fields.Int(required=True, load_only = True)
    bpn = fields.Nested(BpnBaseSchema(), dump_only=True)
    


