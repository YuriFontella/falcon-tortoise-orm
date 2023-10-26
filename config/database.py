import configparser, os

from tortoise import Tortoise, connections

config = configparser.ConfigParser()
config.read('config.ini')

env = os.environ.get('PYTHON_ENV', 'development')

class Database:
    db_url = config.get(env, 'DB_URL')
    modules = {'models': ['src.models.source']}
    generate_schemas = True

    async def process_startup(self, scope, event):
        await Tortoise.init(db_url=self.db_url, modules=self.modules)
        if self.generate_schemas:
            await Tortoise.generate_schemas()

    async def process_shutdown(self, scope, event):
        await connections.close_all()
