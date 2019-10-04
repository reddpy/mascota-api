from app import db

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Test {}>'.format(self.test)    