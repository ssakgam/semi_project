from django.shortcuts import render

# Create your views here.

def homeshow(request):
    return render(request, "homeview/show.html")


def index(request):
    return render(request, 'homeview/show2.html')