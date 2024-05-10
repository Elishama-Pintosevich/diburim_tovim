from marshmallow import Schema, fields

class MailSend(Schema):   
    email = fields.Email()
    subject = fields.Str()
    message = fields.Str()
