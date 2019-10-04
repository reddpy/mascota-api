from flask_restful import Resource,reqparse
from app import db
from models.user import User
from models.pet import Pet
from models.address import Address
from sqlalchemy.exc import SQLAlchemyError

class PeopleRec(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, help='email of the user', required=True, trim=True)
    

    def get(self):
        args = self.parser.parse_args(strict=True)

        current_user = User.query.filter_by(email=args['email']).first()

        if current_user is not None:
            try:
                try:
                    current_address = Address.query.join(User).filter(User.email==current_user.email).first()
                    current_city = current_address.city
                except:
                    return {"message":"error processing request"}                    

                try:
                    all_users = User.query.join(Address).filter(Address.city == current_city, \
                        User.id!=current_user.id).all()
                except:
                    return {"message":"error processing request"}

                people_list = list()
                for row in all_users:
                    temp_dict = dict()
                    temp_dict['id'] = row.id
                    temp_dict['first_name'] = row.first_name
                    temp_dict['last_name'] = row.last_name
                    temp_dict['email'] = row.email
                    temp_dict['primary_phone'] = row.primary_phone
                    people_list.append(temp_dict)

                return people_list

                

            except:
                return {"message":"error processing request"}
