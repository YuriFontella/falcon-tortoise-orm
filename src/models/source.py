from tortoise.models import Model
from tortoise import fields

class Users(Model):
    id=fields.IntField(pk=True)
    name=fields.CharField(max_length=200)