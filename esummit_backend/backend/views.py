from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import *

# Create your views here.


@api_view(['POST'])
def notify(request):
    reqData = request.data
    event = Event.objects.get(id=reqData['event_id'])
    if(Notify.objects.filter(email=reqData['email'], event=event).exists() or Notify.objects.filter(phone=reqData['phone'], event=event).exists()):
        return Response({'status': 'Already Registered'})

    n = Notify.objects.create()
    n.email = reqData['email']
    n.phone = reqData['phone']
    n.event = event
    return Response({'status':"Success"})