from sanic.views import HTTPMethodView
from sanic.response import text


class Greeting(HTTPMethodView):

    def get(self, request):
        return text('Hi man')

    def post(self, request):
        return text('Hello man')
