from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Home page')

def say_hello(request):
    #return HttpResponse('Hello World') #This returns a httpResponse with a simple text.
    return render(request, 'hello.html', {'name':'Bob'}) # Includes a context object that is passed to the template
