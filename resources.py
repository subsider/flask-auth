from flask_restful import Resource


class UserRegistration(Resource):
    @staticmethod
    def post():
        return {'message': 'User registration'}


class UserLogin(Resource):
    @staticmethod
    def post():
        return {'message': 'User login'}


class UserLogoutAccess(Resource):
    @staticmethod
    def post():
        return {'message': 'User logout'}


class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}


class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}


class AllUsers(Resource):
    def get(self):
        return {'message': 'List of users'}

    def delete(self):
        return {'message': 'Delete all users'}


class SecretResource(Resource):
    def get(self):
        return {'answer': 42}