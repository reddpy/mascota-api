from flask_restful import Resource,reqparse
from app import db
from models.user import User
from models.address import Address
from utils.password import hash_password, verify_password

class Register(Resource):

    def max_phone_length(max_length):
        def validate(s):
            if len(s) <= max_length:
                return s
            raise ValidationError("Phone must be no more than {} characters long",max_length)
        return validate

    parser = reqparse.RequestParser()
    parser.add_argument('first_name', type=str, help='first name of user', required=True, trim=True)
    parser.add_argument('last_name', type=str, help='last name of user', required=True, trim=True)
    parser.add_argument('email', type=str, help='email of the user', required=True, trim=True)
    parser.add_argument('password', type=str, help='password of the user', required=True, trim=True)
    parser.add_argument('primary_phone', type=max_phone_length(15), help='phone of the user', required=True, trim=True)

    parser.add_argument('addr_1', type=str, help='address 1 of user', required=True, trim=True)
    parser.add_argument('addr_2', type=str, help='address 2 of user', required=True, trim=True)
    parser.add_argument('city', type=str, help='city of the user', required=True, trim=True)
    parser.add_argument('state', type=str, help='state of the user', required=True, trim=True)
    parser.add_argument('zip_code', type=str, help='zip code of the user', required=True, trim=True)

    def post(self):
        args = self.parser.parse_args(strict=True)

        email = args['email']
        primary_phone = args['primary_phone']

        email_user = User.query.filter_by(email=email).first()
        phone_user = User.query.filter_by(primary_phone=primary_phone).first()

        if email_user is not None:
            return {"message":"User with this email already exists"}, 422

        if phone_user is not None:
            return {"message":"User with this phone already exists"}, 422


        password = hash_password(args['password'])
        del args['password']

        try:
            try:
                new_user = User(first_name=args['first_name'],last_name=args['last_name'], \
                    password=password, email = args['email'], primary_phone=args['primary_phone'])

                db.session.add(new_user)
                db.session.commit()
            except:
                db.session.rollback()
                return {"message":"Internal error, could not create user"}, 400 

            try:
                new_address = Address(addr_1=args['addr_1'], addr_2=args['addr_2'], city=args['city'], \
                    state=args['state'], zip_code=args['zip_code'], user_id=User.query.filter_by(email=email).first().id)
                
                db.session.add(new_address)
                db.session.commit()

            except:
                db.session.rollback()
                db.session.delete(new_user)
                db.session.commit()
                return {"message":"Internal error, could not create user"}, 400

        except:
            return {"message":"Internal error, could not create user"}, 400

        return args
