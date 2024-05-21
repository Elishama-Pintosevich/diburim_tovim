from db import db
from sqlalchemy.sql import func

class CalendarModel(db.Model):
    __tablename__ = "calendar"

    id = db.Column(db.Integer, primary_key = True)
    bpn_id = db.Column(db.Integer, unique = True, nullable = False)
    taken_date = db.Column(db.Integer, nullable = False)
    time_created = db.Column(db.DateTime(timezone = True), server_default = func.now())
    time_updated = db.Column(db.DateTime(timezone = True), onupdate = func.now())