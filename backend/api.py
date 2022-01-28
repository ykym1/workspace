from flask import Blueprint, request
from flask_restful import Api, Resource
from editImage import edit

api_bp = Blueprint('api', __name__, url_prefix='/api')


class Spam(Resource):
    def get(self):
        return {'id': 42, 'name': 'Name'}


class Test(Resource):
    def get(self):
        return "aaaaaaaaaaaaaaa1"


class PostTest(Resource):
    def post(self):
        json = request.get_json(force=True)
        return {'json_request': json}


class EditImage(Resource):
    def post(self):
        json = request.get_json(force=True)

        result_image = edit(json["image"])
        return {"image": result_image}


api = Api(api_bp)
api.add_resource(Spam, '/spam')
api.add_resource(Test, '/test')
api.add_resource(PostTest, '/postTest')
api.add_resource(EditImage, '/editImage')
