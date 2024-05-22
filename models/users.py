from db import db
from sqlalchemy.sql import func

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    phone_number = db.Column(db.Integer, unique = True, nullable = False)
    email = db.Column(db.String(80), nullable = True)
    password = db.Column(db.String(80), nullable = False)
    account = db.Column(db.String(80), nullable = False)
    token = db.Column(db.String(80), nullable = False)
    bpn = db.relationship("BpnModel", back_populates="user", lazy = "dynamic", cascade="all, delete")

    time_created = db.Column(db.DateTime(timezone = True), server_default = func.now())
    time_updated = db.Column(db.DateTime(timezone = True), onupdate = func.now())