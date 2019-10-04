from flask_restful import Resource,reqparse
from app import db
from models.user import User
from models.pet import Pet
from sqlalchemy.exc import SQLAlchemyError

class PetList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, help='email of the user', required=True, trim=True)
    

    def get(self):
        args = self.parser.parse_args(strict=True)

        current_user = User.query.filter_by(email=args['email']).first()

        if current_user is not None:
            try:
                all_pets = Pet.query.filter_by(user_id=current_user.id)
                pets_list = list()

                for row in all_pets:
                    temp_dict = dict()
                    temp_dict['id'] = row.id
                    temp_dict['name'] = row.name
                    temp_dict['pet_type'] = row.pet_type
                    temp_dict['breed'] = row.breed
                    temp_dict['description'] = row.description
                    temp_dict['age'] = row.age
                    temp_dict['weight'] = row.weight
                    temp_dict['user_id'] = row.user_id
                    pets_list.append(temp_dict)

                return pets_list

            except:
                return {"message":"error processing request"}

