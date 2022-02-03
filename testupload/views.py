from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.method == 'POST':  # If the form has been submitted...
        data= request.POST.get("firstname")
        print(data)

    return render(request,"index.html")
def start(request):
    return HttpResponse("go to apps")