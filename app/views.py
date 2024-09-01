from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def school(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            print(SFDO.cleaned_data)
            return HttpResponse('Data submitted')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'school.html',d)


def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
        else:
            return HttpResponse('Invalid Data')

    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WTFO=WebpageForm()
    d={'WTFO':WTFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=tn)
            n=WFDO.cleaned_data['name']
            ul=WFDO.cleaned_data['url']
            em=WFDO.cleaned_data['email']
            WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=ul,email=em)
            WO.save()
        else:
            return HttpResponse('Invalid Data')

    return render(request,'insert_webpage.html',d)
            


def insert_access(request):
    ATFO=AccessRecordForm()
    d={'ATFO':ATFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            n=AFDO.cleaned_data['name']
            WO=Webpage.objects.get(name=n)
            dt=WFDO.cleaned_data['date']
            au=WFDO.cleaned_data['author']
            AO=AccessRecord.objects.get_or_create(name=AO,date=dt,author=au)
            AO.save()
        else:
            return HttpResponse('Invalid Data')

    return render(request,'insert_access.html',d)