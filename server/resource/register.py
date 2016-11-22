from flask_restplus import Resource, Api
from .. import api

ns = api.namespace('register', description="用户注册")

class Register(Resource):
    """用户注册模块


    """
    def post(self):
        "用户注册"
        return {}


ns.add_resource(Register, '/')
