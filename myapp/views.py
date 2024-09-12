from django.shortcuts import render
from myceleryproject.celery import add
from myapp.tasks import subtract
from celery.result import AsyncResult
# Create your views here.
def index(request):
    print("results : ")
    # enqueue the task
    result = add.delay(10, 15)
    print('result 1: ',result)
    result2 = subtract.delay(20,10)
    print('result 2:',result2)
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

