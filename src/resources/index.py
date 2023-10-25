from src.models.source import Users

class IndexResource:
    async def on_get(self, req, resp):
        users = await Users.first().values('name')
        resp.media = users