from peewee import CharField
from erp_app.models.base import BaseModel


#http://docs.peewee-orm.com/en/latest/peewee/models.html
class Product(BaseModel):
    username = CharField(unique=True)