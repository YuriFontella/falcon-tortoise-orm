from src.models.source import Users

class UsersResource:
    async def on_get(self, req, resp):
        users = await Users.first().values('name')
        resp.media = users