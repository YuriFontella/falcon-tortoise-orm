from src.models.source import Users
from src.storage.limits import limiter

class UsersResource:
    @limiter.limit()
    async def on_get(self, req, resp):
        user = await Users.first().values('name')
        resp.media = user