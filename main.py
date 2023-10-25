import falcon.asgi

from middleware.database import Database
from src.resources.index import IndexResource

app = falcon.asgi.App(middleware=[Database()])

app.add_route('/', IndexResource())
