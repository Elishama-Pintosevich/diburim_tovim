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
    path = fields.Str(required=True)
    kind = fields.Int(required=True)
    parameters = fields.Str(required=False)
    

class CalendarBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    taken_date = fields.Date()
    room_number = fields.Int(required=True)

class SoundBaseSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True)
    type = fields.Str(required=True)
    path = fields.Str(dump_only=True)
    bpn = fields.Str(required=True) 

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
    sounds = fields.List(fields.Nested(SoundBaseSchema()), dump_only=True) 


class CalendarSchema(CalendarBaseSchema):
    bpn_id = fields.Int(required=True, load_only = True)
    bpn = fields.Nested(BpnBaseSchema(), dump_only=True)

class SoundSchema(SoundBaseSchema):
    action_id = fields.Int(required=True, load_only = True)
    action = fields.Nested(ActionsBaseSchema(), dump_only=True)
    


