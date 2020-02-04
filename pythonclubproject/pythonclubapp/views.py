from django.shortcuts import render

# Create your views here.
def index(request):
    #when requests comes in, this function says where to find the page:
    return render(request, 'pythonclubapp/index.html')
    