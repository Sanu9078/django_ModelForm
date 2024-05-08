from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    TO=TopicModel()
    d={'TO':TO}
    if request.method == 'POST':
        TFDO=TopicModel(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse("Done")
        return HttpResponse("Invalid Data")
    return render(request,'insert_topic.html',d)

def insert_website(request):
    WO=WebsiteModel()
    d={'WO':WO}
    if request.method == 'POST':
        WFDO=WebsiteModel(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse("Done")
        return HttpResponse("Invalid Data")
    return render(request,'insert_website.html',d)

def insert_access(request):
    AO=AccessModel()
    d={'AO':AO}
    if request.method == 'POST':
        AFDO=AccessModel(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse("Done")
        return HttpResponse("Invalid Data")
    return render(request,'insert_access.html',d)