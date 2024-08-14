from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField, TextField, ForeignKey, URLField, CASCADE, ImageField
from apps.account.choices import AccountRole
from apps.shared.models import BaseModel


class Account(BaseModel, AbstractUser):
    role = CharField(max_length=128, choices=AccountRole.choices, default=AccountRole.MEMBER)
    is_subscribe = BooleanField(default=False)


class Feed(BaseModel):
    name = CharField(max_length=128)
    body = TextField(blank=True, null=True)
    website = URLField(blank=True, null=True)
    account = ForeignKey('account.Account', CASCADE, 'feeds')


class Blog(BaseModel):
    title = CharField(max_length=128)
    body = TextField(max_length=128)
    image = ImageField(upload_to='blog/images/')
    owner = ForeignKey('account.Account', CASCADE, 'blogs')