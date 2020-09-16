from datetime import datetime
from mongoengine import Document, StringField, DateField, ReferenceField, ListField


class Audit(Document):
    email = ReferenceField("Admin", required=True)
    action = ListField(required=True)
    created_at = DateField(default=datetime.strftime(datetime.today(), "%a %d-%m-%Y %H:%M:%S"))


