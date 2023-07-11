from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, "core/home.html")

def list (request):
    return render(request, "core/list.html")

def contact (request):
    return render(request, "core/contact.html")
