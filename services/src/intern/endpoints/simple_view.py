from sanic.views import HTTPMethodView
from sanic.response import text


class SimpleView(HTTPMethodView):

    def get(self, request):
        return text('I am get method')

    def post(self, request):
        return text('I am post method')
