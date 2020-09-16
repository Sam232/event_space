from datetime import datetime
from mongoengine import Document, StringField, DateField, BooleanField


class Business(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    mobile = StringField(required=True, max_length=12)
    business_type = StringField(required=True)
    about = StringField(required=True, max_length=125)
    portfolio_website = StringField(required=False)
    fb_fan_page = StringField(required=False)
    ig_fan_page = StringField(required=False)
    created_at = DateField(default=datetime.strftime(datetime.today(), "%a %d-%m-%Y %H:%M:%S"))
    updated_at = DateField(required=False)
    approved = BooleanField(required=True, default=False)


