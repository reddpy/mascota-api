from flask_restful import Resource,reqparse
from app import db
from models.user import User
from models.pet import Pet
from sqlalchemy.exc import SQLAlchemyError

class PetSingle(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, help='email of the user', required=True, trim=True)
    parser.add_argument('name', type=str, help='name of the pet', required=True, trim=True)
    parser.add_argument('pet_type', type=str, help='type of the pet', required=True, trim=True)
    parser.add_argument('breed', type=str, help='breed of the pet', required=True, trim=True)
    parser.add_argument('description', type=str, help='description of the pet', required=True, trim=True)
    parser.add_argument('age', type=int, help='age of the pet', required=True, trim=True)
    parser.add_argument('weight', type=float, help='weight of the pet', required=True, trim=True)


    get_parser = reqparse.RequestParser()
    get_parser.add_argument('email', type=str, help='email of the user', required=True, trim=True)
    get_parser.add_argument('id', type=int, help='id of the pet', required=True, trim=True)

    def get(self):
        args = self.get_parser.parse_args(strict=True)
        current_user = User.query.filter_by(email=args['email']).first()

        if current_user is not None:
            try:
                pet_obj = Pet.query.get(args['id'])

                if pet_obj is not None:
                    return {
                        "id":pet_obj.id,
                        "name":pet_obj.name,
                        "pet_type":pet_obj.pet_type,
                        "breed":pet_obj.breed,
                        "description":pet_obj.description,
                        "age":pet_obj.age,
                        "weight":pet_obj.weight
                    }
                else:
                    return {"message":"pet not found"}
            except:
                return {"message":"error processing request"}




    def post(self):
        args = self.parser.parse_args(strict=True)
        current_user = User.query.filter_by(email=args['email']).first()

        if current_user is not None:
            try:
                new_pet = Pet(name=args['name'], pet_type=args['pet_type'], breed=args['breed'], \
                    description=args['description'], age=args['age'], weight=args['weight'], user_id=current_user.id)
                
                db.session.add(new_pet)
                db.session.commit()
                db.session.refresh(new_pet)

                args['id'] = new_pet.id
                del args['email']
                
                return args

            except Exception as e:
                print(e)
                db.session.rollback()
                return {"message":"Internal error, could not create Pet"}, 400  

        else:
            return {"message":"Internal error, could not create Pet"}, 400  