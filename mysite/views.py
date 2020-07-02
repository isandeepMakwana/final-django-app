#from django.http import HttpResponse
from django.shortcuts import render
#import datetime
books = [
    {
        "book_name":"Marchent of Venic",
        "book_author":"W. Shankspear",
        "book_price":300


    },
    {
        "book_name":"Gaban",
        "book_author":"Premchand",
        "book_price":250


    },
    ]


def index(request, name = 'Sandeep Makwana'):
    #return HttpResponse("<h1><center> Welcome to Sandeep first Django project</center></h1>")
    return render(request, 'index.html',{'authorname':name})

    
def about(request, number=(-5)):
    #return HttpResponse("<h1><center> This is about page</center></h1>")
    return render(request, 'about.html',{'books':books,'num':number})


def contact(request):
    #return HttpResponse("<h1><center> This is contact as  page</center></h1>")
    return render(request, 'contact.html')

def result(request):
    val1 = int(request.POST["t1"])
    val2 = int(request.POST["t2"])
    sum = val1 + val2

    return render(request, 'result.html' ,{'result': sum})
