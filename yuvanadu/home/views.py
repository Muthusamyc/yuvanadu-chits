from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def securitiesacceptable(request):
    return render(request,"securities acceptable.html")

def payment(request):
    return render(request,"payment.html")

def contact(request):
    return render(request,"contact.html")

def productandservice(request):
    return render(request,"productandservice.html")

