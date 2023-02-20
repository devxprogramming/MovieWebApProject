from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

# This is the Login Function

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

# This is the Pricing Page

def pricing(request):
    return render(request, 'pricing.html')

# Helping And FAQ Page

def faq(request):
    return render(request, 'faq.html')