from intern.core import app
from intern.endpoints.simple_view import SimpleView
from intern.endpoints.greeting import Greeting


app.add_route(SimpleView.as_view(), '/simpleview')
app.add_route(Greeting.as_view(), '/greeting')

app.run(host='0.0.0.0', port=8000)
