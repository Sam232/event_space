from datetime import datetime
from mongoengine import Document, StringField, DateField, ReferenceField


class AcceptedRequest(Document):
    event_id = ReferenceField("Event", required=True)
    business_id = ReferenceField("Business", required=True)
    created_at = DateField(default=datetime.strftime(datetime.today(), "%a %d-%m-%Y %H:%M:%S"))


