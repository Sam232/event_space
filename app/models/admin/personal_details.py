from datetime import datetime
from mongoengine import Document, StringField, DateField, BooleanField


class Admin(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    mobile = StringField(required=True, max_length=12)
    type = StringField(choices=["SUPER", "NORMAL"])
    created_at = DateField(default=datetime.strftime(datetime.today(), "%a %d-%m-%Y %H:%M:%S"))
    updated_at = DateField(required=False)


