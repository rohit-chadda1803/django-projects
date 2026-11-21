from django.urls import  path
from django.http import HttpResponse 

def dummy_note(request):
    return HttpResponse("pdhle bhai")

urlpatterns = [

    path('' , dummy_note) , 
]