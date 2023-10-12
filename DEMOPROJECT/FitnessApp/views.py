from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Hi(request):
    return render(request, 'FitnessApp/webpage.html')
