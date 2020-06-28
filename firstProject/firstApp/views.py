from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #to print something or giving a response we have to use HttpResponse
    #return HttpResponse('Hello World')
    #to render a html page & using dynamic naming
    return render(request, 'home.html', {'name' : 'Swaniket'})

#writhing the function for add
def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    res = val1 + val2
    return render(request, 'result.html', {'result': res})
