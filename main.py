import falcon.asgi

from config.database import Database

from src.resources.users import UsersResource
from src.storage.transform import extra_handlers
from src.storage.error import StorageError
from src.storage.limiter import Limiter

app = falcon.asgi.App(middleware=[Database(), Limiter()])

app.add_route('/users', UsersResource())

app.resp_options.media_handlers.update(extra_handlers)
app.req_options.media_handlers.update(extra_handlers)

app.add_error_handler(Exception, StorageError.handle)