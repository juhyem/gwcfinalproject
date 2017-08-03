from django import forms
from django.contrib.admin.widgets import AdminTimeWidget, AdminDateWidget
from .models import Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title', 'cause', 'street_address', 'name_of_place', 'start_date_and_time', 'end_date_and_time', 'first_name', 'last_name', 'email', 'phone', 'description')


    # start_time = forms.TimeField(widget = AdminTimeWidget)
    # start_date = forms.DateField(widget = AdminDateWidget)




# class Event(models.Model):
#     # user info
#     first_name = models.CharField(max_length=30)
#     last_name= models.CharField(max_length=30)
#     email = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#     # event
#     title = models.CharField(max_length=200)
#     cause = models.CharField(max_length=200)
#     # location
#     street_address = models.CharField(max_length=150)
#     name_of_place_opt = models.CharField(max_length=150)
#     # time
#     date_of_event = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     description = models.TextField()
#     published_date = models.DateTimeField(
#             blank=True, null=True)
