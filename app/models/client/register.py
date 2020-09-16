from datetime import datetime
from mongoengine import Document, StringField, DateField


class Register(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    mobile = StringField(required=True, max_length=12)
    created_at = DateField(default=datetime.strftime(datetime.today(), "%a %d-%m-%Y %H:%M:%S"))
    updated_at = DateField(required=False)


