from rest_framework import viewsets
from django.shortcuts import redirect,render,HttpResponse
from .forms import *
from .serializers import *
from .models import *


def home(request):
    return render(request,'home.html')

class ARViewSet(viewsets.ModelViewSet):
    queryset = AR.objects.all().order_by('name')
    serializer_class = ARSerializer
    http_method_names = ['get']


class smgViewSet(viewsets.ModelViewSet):
    queryset = smg.objects.all().order_by('name')
    serializer_class = smgSerializer
    http_method_names = ['get']

class lmgViewSet(viewsets.ModelViewSet):
    queryset = lmg.objects.all().order_by('name')
    serializer_class = lmgSerializer
    http_method_names = ['get']

class dmrViewSet(viewsets.ModelViewSet):
    queryset = dmr.objects.all().order_by('name')
    serializer_class = dmrSerializer
    http_method_names = ['get']

class sniperViewSet(viewsets.ModelViewSet):
    queryset = sniper.objects.all().order_by('name')
    serializer_class = sniperSerializer
    http_method_names = ['get']

class shotgunViewSet(viewsets.ModelViewSet):
    queryset = shotgun.objects.all().order_by('name')
    serializer_class = shotgunSerializer
    http_method_names = ['get']

class pistolViewSet(viewsets.ModelViewSet):
    queryset = pistol.objects.all().order_by('name')
    serializer_class = pistolSerializer
    http_method_names = ['get']

class otherViewSet(viewsets.ModelViewSet):
    queryset = other.objects.all().order_by('name')
    serializer_class = otherSerializer
    http_method_names = ['get']

class healthViewSet(viewsets.ModelViewSet):
    queryset = health.objects.all().order_by('name')
    serializer_class = healthSerializer
    http_method_names = ['get']

class gripViewSet(viewsets.ModelViewSet):
    queryset = grip.objects.all().order_by('name')
    serializer_class = gripSerializer
    http_method_names = ['get']

# def contact(request):
#     if request.method=='POST':
#          email = request.POST.get('email')
#          message = request.POST.get('message')
#          contact = ContactForm(email=email,message=message)
#          if contact.is_valid():
#             contact.save()
#             return redirect('success')


#     return render(request,'home.html')



def success(request):
    return render(request,'success.html')

def home(request):
    if request.method=='POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        data={'email':email,'message':message}
        contact = ContactForm(data=data)
        # print(email)
        # print(message)
        if contact.is_valid():
            contact.save()
            return redirect('success')
    notifys=Notify.objects.all()
    params={'notifys':notifys}
    return render(request,'home.html',params)


