from src.storage.limiter import limiter
from src.models.main import Users

@limiter.limit()
class UsersResource:
    async def on_get(self, req, resp):
        user = await Users.first().values('name')
        resp.media = user
