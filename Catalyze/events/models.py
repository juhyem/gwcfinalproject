from django.db import models

# Create your models here.
# Create an event
# -------------------
# # User info
#     name
#     email
#     phone
# Event info
#     title
#     cause/purpose
#     location
#         street address
#         name of place
#     time
#         start time
#         end time
#     description
#     picture
#     permit

from django.db import models
from django.utils import timezone


class Event(models.Model):
    # user info
    first_name = models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    # event
    title = models.CharField(max_length=200)
    cause = models.CharField(max_length=200)
    # location
    street_address = models.CharField(max_length=150)
    name_of_place = models.CharField(max_length=150)
    # time
    start_date_and_time = models.DateTimeField()
    end_date_and_time = models.DateTimeField()
    description = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)
    # image = models.ImageField(upload_to=
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
