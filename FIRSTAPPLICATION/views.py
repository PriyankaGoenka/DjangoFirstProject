from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def style(request):
    return render(request,'firstapp/second.html')

def app(request):
    return render(request,'firstapp/first.html')

def home(request):
    return HttpResponse("Hello Candidates!! GoodMorning, welcome to Djanjo Training!")

def about(request):
    return HttpResponse("Welcome to the about us page!")

def contact(request):
    return HttpResponse("Welcome to the contact us page!")