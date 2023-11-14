import falcon

class StorageError(Exception):
	@staticmethod
	async def handle(req, resp, e, params):
		print(e)
		raise falcon.HTTPInternalServerError(description=str(e))