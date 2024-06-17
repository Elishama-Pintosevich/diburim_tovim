from db import db
from sqlalchemy.sql import func

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    phone_number = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(80), nullable = True)
    password = db.Column(db.String(200), nullable = False)
    account = db.Column(db.String(200), nullable = True)
    # token = db.Column(db.String(200), nullable = False)
    api_key = db.Column(db.String(200), nullable = True)
    api_secret = db.Column(db.String(200), nullable = True)
    bpn = db.relationship("BpnModel", back_populates="user", lazy = "dynamic", cascade="all, delete")

    time_created = db.Column(db.DateTime(timezone = True), server_default = func.now())
    time_updated = db.Column(db.DateTime(timezone = True), onupdate = func.now())