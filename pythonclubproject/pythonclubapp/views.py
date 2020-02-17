from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event 

# Create your views here.
def index(request):
    #when requests comes in, this function says where to find the page:
    return render(request, 'pythonclubapp/index.html')
    
def getResources(request): #request is browser asking for a page
    resource_list=Resource.objects.all()#all will return everything but there are other ways to do
    context={'resource_list' : resource_list}#dictionary: set up context: pass the list to the webpage
    return render(request, 'pythonclubapp/resources.html', context=context) #this could be just the curly braces, you basically set up a variable above
    #the name of html page has to match exactly the page inside the templates/pythonclubapp

def getMeetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'pythonclubapp/meetings.html', {'meeting_list' : meeting_list})
    #this is an alternative way to do the same as getResources w/o setting up variable
    #context= before. you can just add to the return render line.

def meetingDetails(request, id): #passing request and an ID. we will choose one of the meeting and show details for it
    meet=get_object_or_404(Meeting, pk=id) #get instead of all: you are looking for one object
    return render(request, 'pythonclubapp/meetingdetails.html', {'meet': meet})