from django.shortcuts import render

from app.models import *

from django.db.models.functions import Length

from django.db.models import Q
# Create your views here.

def display_topic(request):
    QLTO = Topic.objects.all()
    
    # arranging the data in a order way by ascending and descending order. 
    QLTO = Topic.objects.order_by('topic_name')
    QLTO = Topic.objects.order_by('-topic_name')
    QLTO = Topic.objects.order_by(Length('topic_name'))
    QLTO = Topic.objects.order_by(Length('topic_name').desc())

    d = {'QLTO':QLTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QLWO = Webpage.objects.all()

    '''  From here Orderby clause is used for arranging the data based on our requirement '''
    QLWO = Webpage.objects.order_by('name')
    QLWO = Webpage.objects.order_by('-url')
    QLWO = Webpage.objects.order_by(Length('email').desc())
    

    ''' Here, retrieving the data number of rows as you need like 5 to 10, 6 to 9 by using slicing on list of Query objects '''
    QLWO = Webpage.objects.all()[5:11]
    QLWO = Webpage.objects.all()[:5]

    ''' From here we are accessing the data based on condition using lookups '''
    QLWO = Webpage.objects.filter(id__gt = 6)
    QLWO = Webpage.objects.filter(id__lt = 4)
    QLWO = Webpage.objects.filter(id__gte = 9)
    QLWO = Webpage.objects.filter(id__lte = 2)

    ''' From here We are retriving the data by providing regular expressions in regex lookup'''
    QLWO = Webpage.objects.filter(name__regex = r'i$')

    QLWO = Webpage.objects.filter(email__endswith = 'com')
    QLWO = Webpage.objects.filter(url__endswith = 'in')
    QLWO = Webpage.objects.filter(url__contains = '.in')

    d = {'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def display_access(request):
    QLAO = AccessRecord.objects.all()

    ''' From here we are accessing the data based on condition using date lookups '''
    QLAO = AccessRecord.objects.filter(date__day = '22')
    QLAO = AccessRecord.objects.filter(date__year = '2019')
    QLAO = AccessRecord.objects.filter(date__month = '4')


    ''' From here dealing with mutiple conditions '''
    ''' So to achieve that multiple conditions we need to use Q objects ... '''
    ''' Soo import from django.db.models import Q'''
    ''' We can write multiple condtions inside filter in case of and '''
    ''' We should use Q objects when conditions are dealing with or conditions '''

    QLAO = AccessRecord.objects.filter(Q(author__startswith = 'r') | Q(author__startswith = 'h'))
    QLAO = AccessRecord.objects.filter(Q(author__regex = '[A-P]') | Q(date__year__gt = 2021))
    QLAO = AccessRecord.objects.filter(Q(author__regex = '[P-T]') & Q(date__year__gt = 2021))
    QLAO = AccessRecord.objects.filter(author__regex = '[P-T]',date__year__gt = 2021)


    d = {'QLAO':QLAO}
    return render(request,'display_access.html',d)

def insert_topic(request):
    tn = input('Enter topic name: ')
    NTO = Topic.objects.get_or_create(topic_name = tn)[0]
    NTO.save()
    QLTO = Topic.objects.all()
    d = {'QLTO':QLTO}
    return render(request,'display_topic.html',d)

def insert_webpage(request):
    tn = input('Enter topic name: ')
    n = input('Enter name : ')
    u = input('Enter URL: ')
    e = input('Enter email: ')
    TO = Topic.objects.get(topic_name = tn)
    NWO = Webpage.objects.get_or_create(topic_name = TO,name = n,url = u,email = e)[0]
    NWO.save()
    QLWO = Webpage.objects.all()
    d = {'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def insert_access(request):
    pk = int(input('Enter pk value for webpage: '))
    a = input('Enter author name: ')
    d = input('Enter date in YYYY-MM-DD')
    WO = Webpage.objects.get(pk = pk)
    NAO = AccessRecord.objects.get(name = WO,author = a,date = d)

    QLAO = AccessRecord.objects.all()
    d = {'QLAO':QLAO}
    return render(request,'display_access.html',d)

