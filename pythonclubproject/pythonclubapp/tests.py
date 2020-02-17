from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .views import index, getResources, getMeetings, meetingDetails
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class MeetingTest(TestCase):
    def setup(self):
        meet=Meeting(meeting_title='IceBreaker')
        resource=Resource(resource_name='HTML', resource_type='video')
        return resource

    def test_string(self):
        test=self.setup()
        self.assertEqual(str(test), test.resource_name)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourceTest(TestCase):
    def test_string(self):
        resource2=Resource(resource_name='CSS/Java', resource_type='short course')
        self.assertEqual(str(resource2), resource2.resource_name)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class MeetingMinutesTest(TestCase):
    def test_string(self):
        minutes=MeetingMinutes(minutes_text='we talked about many things')
        self.assertEqual(str(minutes), minutes.minutes_text)

    def test_table(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class EventTest(TestCase):
    def test_string(self):
        event=Event(event_title='Improving your HTML')
        self.assertEqual(str(event), event.event_title)
    
    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

#class IndexTest(TestCase):
#    def test_view_url_accessible_by_name(self):
 #       response = self.client.get(everse('index'))
  #      self.assertEqual(response.status_code,200)

#class getResources(TestCase):
 #   def test_view_url_accessible_by_name(self):
  #      response=self.client.get(reverse('resources'))
   #     self.assertEqual(response.status_code,200)