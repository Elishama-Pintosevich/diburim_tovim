from db import db
from sqlalchemy.sql import func

class ActionModel(db.Model):
    __tablename__ = "actions"

    id = db.Column(db.Integer, primary_key = True)
    bpn_id = db.Column(db.Integer, db.ForeignKey("bpn.id"), nullable = False)
    bpn = db.relationship("BpnModel", back_populates="actions")
    kind = db.Column(db.Integer, nullable = False)
    path = db.Column(db.String(10), nullable = False)
    paramaters = db.Column(db.String(1000), nullable=False)

    time_created = db.Column(db.DateTime(timezone = True), server_default = func.now())
    time_updated = db.Column(db.DateTime(timezone = True), onupdate = func.now())