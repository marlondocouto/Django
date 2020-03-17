from django.shortcuts import render
from .models import StockType, StockPerformance, FinanceResource
from .forms import StockTypeForm, StockPerformanceForm, FinanceResourceForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'stocktrackingapp/index.html')

def gettype(request):
    type_list=StockType.objects.all()
    return render(request,'stocktrackingapp/types.html', {'type_list':type_list})

def getperformances(request):
    performances_list=StockPerformance.objects.all()
    return render(request, 'stocktrackingapp/performances.html', {'performances_list': performances_list})

def getresources(request):
    resources_list=FinanceResource.objects.all()
    return render(request, 'stocktrackingapp/resources.html', {'resources_list':resources_list})

@login_required
def newStockType(request):
    form=StockTypeForm
    if request.method=='POST':
        form=StockTypeForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=StockTypeForm()
    else:
        form=StockTypeForm()
    return render(request, 'stocktrackingapp/newstocktype.html', {'form':form})

def newStockPerformance(request):
    form=StockPerformanceForm
    if request.method=='POST':
        form=StockPerformanceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=StockPerformanceForm
    else:
        form=StockPerformanceForm()
    return render(request, 'stocktrackingapp/newstockperformance.html', {'form':form})

def newFinanceResource(request):
    form=FinanceResourceForm
    if request.method=='POST':
        form=FinanceResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=FinanceResourceForm
    else:
        form=FinanceResourceForm()
    return render(request, 'stocktrackingapp/newfinanceresource.html', {'form':form})

def loginmessage(request):
    return render(request, 'stocktrackingapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'stocktrackingapp/logoutmessage.html')