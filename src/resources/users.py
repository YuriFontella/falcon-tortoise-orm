from src.models.main import Users

class UsersResource:
    async def on_get(self, req, resp):
        user = await Users.first().values('name')
        resp.media = user
