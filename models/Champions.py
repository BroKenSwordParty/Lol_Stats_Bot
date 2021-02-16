from orm import Model
from peewee import *

db = SqliteDatabase('db.sqlite')


class BaseModel(Model):
    class Meta:
        database = db


class Champion(BaseModel):
    id = IntegerField(primary_key=True, unique=True)
    name = CharField()
