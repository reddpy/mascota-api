from app import db
from .user import User

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    addr_1 = db.Column(db.String(64))
    addr_2 = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    zip_code = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    def __repr__(self):
        return '<Address {}, {}, {}, {}, {}, {}, {}>'.format(self.id, self.addr_1, self.addr_2, self.city, self.state, self.zip_code, self.user_id)    