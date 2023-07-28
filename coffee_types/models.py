import uuid

from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model

User = get_user_model()


class Coffee(models.Model):
    '''
    link coffeetype to the manager that made the coffeetype itself.
    '''
    class PremiumType(models.TextChoices):
        FOR_PREMIUM_USERS = 'For Premium'
        FOR_REGULAR_USERS = 'For regular'

    store_manager_email = models.EmailField(max_length=79)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.IntegerField()
    coffee_type = models.CharField(
        max_length=79,
        choices=PremiumType.choices,
        default=PremiumType.FOR_REGULAR_USERS
    )
    main_photo = models.ImageField(upload_to='coffeeTypes/')
    photo_1 = models.ImageField(upload_to='coffeeTypes/')
    photo_2 = models.ImageField(upload_to='coffeeTypes/')
    is_published = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=now)

    def delete(self):
        '''
        When coffee obj gets deleted,
        images should be deleted from the store.
        '''
        self.main_photo.storage.delete(self.main_photo.name)
        self.photo_1.storage.delete(self.photo_1.name)
        self.photo_2.storage.delete(self.photo_2.name)

        super().delete()

    def __str__(self):
        return self.title


class Order(models.Model):
    '''handles the coffee orders'''
    coffee = models.ForeignKey(Coffee, on_delete=models.DO_NOTHING, null=True)
    identifier = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.coffee.title
