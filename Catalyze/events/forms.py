from django import forms
# from django.contrib.admin.widgets import AdminTimeWidget, AdminDateWidget
from .models import Event
from django.forms import DateTimeField

class EventForm(forms.ModelForm):

    # start_date_and_time = DateTimeField(input_formats=["%m/%d/%y %H:%M'"])
    # end_date_and_time = DateTimeField(input_formats=["%m/%d/%y %H:%M'"])
    class Meta:
        model = Event
        fields = ('title', 'cause', 'street_address', 'city', 'state', 'zip_code', 'name_of_place', 'start_date_and_time', 'end_date_and_time', 'first_name', 'last_name', 'email', 'phone', 'description', 'image')

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
