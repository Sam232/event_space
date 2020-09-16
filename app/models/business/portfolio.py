from datetime import datetime
from mongoengine import Document, StringField, DateField, ListField, ReferenceField


class Portfolio(Document):
    business_id = ReferenceField("Business", required=True)
    name = StringField(required=True)
    about = StringField(required=True, max_length=125)
    images = ListField(required=False)
    created_at = DateField(default=datetime.strftime(datetime.today(), "%a %d-%m-%Y %H:%M:%S"))
    updated_at = DateField(required=False)


