from datetime import datetime
from mongoengine import Document, StringField, DateField


class PendingRequest(Document):
    event_id = StringField(required=True)
    business_id = StringField(unique=True, required=True)
    created_at = DateField(default=datetime.strftime(datetime.today(), "%a %d-%m-%Y %H:%M:%S"))


