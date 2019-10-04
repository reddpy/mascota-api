from app import db
from .user import User

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    pet_type = db.Column(db.String(64))
    breed = db.Column(db.String(64))
    description = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    age = db.Column(db.Integer)
    weight = db.Column(db.Float)

    def __repr__(self):
        return '<Pet {}, {}, {}, {}, {}, {}>'.format(self.id, self.name, self.pet_type, self.breed, self.description, self.user_id)  
