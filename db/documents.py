from mongoengine import *


connect('instagram')


class UsersLocationsKievPost(Document):
    nick_name = StringField()
    post_likes = IntField()
    date = DateTimeField()

