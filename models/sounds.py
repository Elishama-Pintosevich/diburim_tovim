from db import db
from sqlalchemy.sql import func

class SoundModel(db.Model):
    __tablename__ = "sounds"

    id = db.Column(db.Integer, primary_key = True)
    action_id = db.Column(db.Integer, db.ForeignKey("actions.id"), nullable = False)
    action = db.relationship("ActionModel", back_populates="sounds")
    type = db.Column(db.String, nullable = False)
    path = db.Column(db.String(200), nullable = False)
    content = db.Column(db.String(1000), nullable=False)
    bpn = db.Column(db.String(20), nullable = False)

    time_created = db.Column(db.DateTime(timezone = True), server_default = func.now())
    time_updated = db.Column(db.DateTime(timezone = True), onupdate = func.now())