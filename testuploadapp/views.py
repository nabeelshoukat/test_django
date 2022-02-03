from django.http import HttpResponse
from django.shortcuts import render
from . import models

def index(request):
    if request.method == 'POST':  # If the form has been submitted...
        fname= request.POST.get("firstname")
        laname= request.POST.get("lastname")
        p = models.person(firstname=fname, lastname=laname)
        p.save()
    return render(request,"index.html")
