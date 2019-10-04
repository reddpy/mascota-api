from flask_restful import Resource,reqparse
from app import db
from app import app
from models.user import User
import requests

class PFDataOrg(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, help='email of the user', required=True, trim=True)
    parser.add_argument('access-token', type=str, help='access token required for api access', required=True, trim=True)
    parser.add_argument('org-id', type=str, help='organization id', required=True, trim=True)

    def get(self):
        args = self.parser.parse_args(strict=True)

        current_user = User.query.filter_by(email=args['email']).first()

        if current_user is not None:

            headers = {
                "Authorization": "Bearer " + args['access-token']
                }

            url = "https://api.petfinder.com/v2/organizations/{}".format(args['org-id'])

            try:
                response = requests.get(url, headers=headers)
            except:
                return {"message":"error, could not connect to the Pet Finder API, please try again later"}

            json_response = response.json()
            return json_response 