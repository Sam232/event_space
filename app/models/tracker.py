from datetime import datetime

from mongoengine import Document, StringField, DateField


class Tracker(Document):
    user_id = StringField(required=True)
    type = StringField(choices=["BUSINESS", "CLIENT"])
    logged_in_at = DateField(required=True)
    logged_out_out = DateField(required=True)

