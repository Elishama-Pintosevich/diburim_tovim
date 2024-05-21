from db import db
from sqlalchemy.sql import func

class BpnModel(db.Model):
    __tablename__ = "bpn"

    id = db.Column(db.Integer, primary_key = True)
    phone_number = db.Column(db.String(20), unique = True, nullable = False)
    user_id = db.Column(db.Integer, nullable = False)
    time_created = db.Column(db.DateTime(timezone = True), server_default = func.now())
    time_updated = db.Column(db.DateTime(timezone = True), onupdate = func.now())