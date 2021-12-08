from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.

def welcome(request):
    return HttpResponse('<h6>welcome to football</h6>')


def template(request):
    return render(request,'welcome.html',{'name':'Nur'})
