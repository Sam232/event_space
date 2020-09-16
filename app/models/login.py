from datetime import datetime
from mongoengine import Document, StringField, DateField


class Login(Document):
    email = StringField(unique=True, required=True)
    password = StringField(required=True)
    type = StringField(choices=["ADMIN", "BUSINESS", "CLIENT"])
    active = StringField(required=True)
    created_at = DateField(default=datetime.strftime(datetime.today(), "%a %d-%m-%Y %H:%M:%S"))
    updated_at = DateField(required=False)


