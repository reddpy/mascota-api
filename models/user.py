from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(64), index=True)
    password = db.Column(db.String(256))
    primary_phone = db.Column(db.String(15), index=True)
    pet = db.relationship('Pet', backref='User')

    def __repr__(self):
        return '<User {}, {}: {},{}>'.format(self.id, self.email,self.last_name, self.first_name)    
