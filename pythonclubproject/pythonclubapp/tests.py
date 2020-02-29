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

class MeetingMinutes_Form_Test(TestCase):
    def test_typeform_is_valid(self):
        form=MeetingMinutesTest(data={'attendance': "Marlon", 'minutes_text':"bla blah blah"})
        self.assertTrue(form.is_valid())


class New_Resouce_authentication_test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='passpass')
        self.type=ResourceType.objects.create(resource_type='laptop')
        self.resource=Resource.objects.create(resource_name='lalala', resource_type=self.type)

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login/?next=/techapp/newProduct/')

    def test_Logged_in_uses_correct_template(self):
        login=self.client.login(username='testuser1', password='P@ssw0rd1')
        response=self.client.get(reverse('newproduct'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'techapp/newproduct.html')    