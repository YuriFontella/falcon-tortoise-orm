import falcon.asgi

from config.database import Database
from src.resources.users import UsersResource

app = falcon.asgi.App(middleware=[Database()])

app.add_route('/', UsersResource())
