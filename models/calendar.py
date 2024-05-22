from db import db
from sqlalchemy.sql import func

class CalendarModel(db.Model):
    __tablename__ = "calendar"

    id = db.Column(db.Integer, primary_key = True)
    bpn_id = db.Column(db.Integer, db.ForeignKey("bpn.id"), nullable = False)
    bpn = db.relationship("BpnModel", back_populates="taken_dates")
    taken_date = db.Column(db.Date, nullable = False)

    time_created = db.Column(db.DateTime(timezone = True), server_default = func.now())
    time_updated = db.Column(db.DateTime(timezone = True), onupdate = func.now())