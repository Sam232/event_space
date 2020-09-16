from datetime import datetime
from mongoengine import Document, StringField, DateField, ListField


class Event(Document):
    client_id = StringField(required=True)
    type = StringField(required=True)
    coordinate = StringField(required=True)  # only show to the accepted business
    about = StringField(required=True)
    payment = StringField(required=True)
    start_date = DateField(required=True)
    end_date = DateField(required=True)
    created_at = DateField(default=datetime.strftime(datetime.today(), "%a %d-%m-%Y %H:%M:%S"))
    updated_at = DateField(required=False)


