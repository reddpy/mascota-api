from flask_restful import Resource,reqparse
from app import db
from app import app
import requests

class PFApiAccess(Resource):

    def get(self):

        request_params = {
            "grant_type": "client_credentials",
            "client_id": app.config['PET_FINDER_API_KEY'],
            "client_secret": app.config['PET_FINDER_CLIENT_KEY']
            }
        try:
            response = requests.post("https://api.petfinder.com/v2/oauth2/token", data=request_params)
        except:
            return {"message":"error, could not connect to the Pet Finder API, please try again later"}

        json_response = response.json()
        return json_response 
    
