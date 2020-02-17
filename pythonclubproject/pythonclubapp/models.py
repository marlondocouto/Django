from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#this is going to map to the database. 

class Meeting(models.Model): #models is a library so this class inherits from the Model class
    meeting_title=models.CharField(max_length=255)
    meeting_date=models.DateField()
    meeting_time=models.TimeField()
    meeting_location=models.CharField(max_length=255)
    meeting_agenda=models.TextField(null=True, blank=True)

    def __str__(self): #what it will show when it prints, for instance
        return self.meeting_title #not so sure what this is doing.

    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

#next class:

class MeetingMinutes(models.Model):
    meeting_id=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    #ABOVE: it refers to the previous table and it requires on what to do on delete
    #Meeting in parenthesis references the previous class.
    attendance=models.ManyToManyField(User)
    minutes_text=models.TextField('Description', blank=True)

    def __str__(self):
        return self.meeting_id

    class Meta:
        db_table='meetingminutes'
        verbose_name_plural='meeting minutes'

#next class:

class Resource(models.Model):
    resource_name=models.CharField(max_length=255)
    resource_type=models.CharField(max_length=255)
    url=models.URLField(null=True, blank=True)
    date_entered=models.DateTimeField()
    user_id=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resource_name

    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

#next class:
class Event(models.Model):
    event_title=models.CharField(max_length=255)
    event_location=models.CharField(max_length=255)
    event_date=models.DateField()
    event_time=models.TimeField()
    event_description=models.TextField()
    user_id=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.event_title

    class Meta:
        db_table='event'
        verbose_name_plural='events'