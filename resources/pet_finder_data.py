from flask_restful import Resource,reqparse
from app import db
from app import app
from models.address import Address
from models.user import User
import requests

class PFDataAnimals(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, help='email of the user', required=True, trim=True)
    parser.add_argument('access-token', type=str, help='access token required for api access', required=True, trim=True)


    def get(self):
        args = self.parser.parse_args(strict=True)

        current_user = User.query.filter_by(email=args['email']).first()

        address = Address.query.filter_by(user_id=current_user.id).first()

        if current_user is not None:
            headers = {
                "Authorization": "Bearer " + args['access-token']
                }

            params = (
                ("type", "dog"),
                # city, state; lat, lot; postal code
                ("location", address.zip_code)
            )
            
            try:
                response = requests.get("https://api.petfinder.com/v2/animals", headers=headers, params=params)
            except:
                return {"message":"error, could not connect to the Pet Finder API, please try again later"}

            json_response = response.json()
            return json_response 

