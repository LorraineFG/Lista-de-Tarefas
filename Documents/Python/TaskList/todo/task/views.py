from tokenize import Name
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloWorld(request):
  return HttpResponse(" Hello World! ")

def taskList(request):
  return render(request, 'task/list.html')

def yourName(request, name):
  return render(request, 'task/yourname.html', {'name': name})