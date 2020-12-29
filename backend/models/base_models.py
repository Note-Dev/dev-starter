from sqlalchemy.dialects.postgresql import JSON
from models import db
class Dummy(db.Model):
    __tablename__ = "dummy"

    id = db.Column(db.Integer, primary_key=True)
    check = db.Column(db.String(255), nullable=False)

    def __init__(self, check):
        self.check = check

    def __repr__(self):
        return "<id {}>".format(self.id)
