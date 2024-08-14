from datetime import timedelta

from django.db.models import CharField, TextField, DateTimeField, TextChoices, Manager, SlugField, ForeignKey, CASCADE, \
    SET_NULL, URLField, DateField, BooleanField
from django.db.models import IntegerField, ImageField
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from apps.article.choices import Status
from apps.article.managers import PublishManager
from apps.shared.models import BaseModel


class Article(BaseModel):

    objects = Manager()
    published = PublishManager()

    title = CharField(max_length=256)
    slug = SlugField(unique=True)
    body = TextField()
    published_at = DateTimeField(default=timezone.now)
    status = CharField(max_length=15, choices=Status.choices, default=Status.DRAFT)
    category = ForeignKey('article.Category', CASCADE, related_name='article')
    likes = IntegerField(default=0)
    image = ImageField(upload_to='article/images')
    owner = ForeignKey('account.Account', SET_NULL, related_name='article', null=True)


class Category(BaseModel):
    name = CharField(max_length=128)


class Comment(BaseModel):
    body = TextField()
    owner = ForeignKey('account.Account', CASCADE, related_name='comments')
    article = ForeignKey('article.Article', CASCADE, related_name='comments')


def advertise_expire(*args, **kwargs):
    return timezone.now() + timedelta(days=3)


class Advertise(BaseModel):
    image = ImageField(upload_to='advertise/images/')
    url = URLField()
    expire_date = DateField(default=advertise_expire)
    phone = PhoneNumberField(region='UZ')
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.url

    def is_expired(self):
        return timezone.now() > self.expire_date


