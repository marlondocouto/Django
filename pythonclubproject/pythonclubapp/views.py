from django.shortcuts import render
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