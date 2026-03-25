from django.shortcuts import render

def home(request):
    return render(request, 'q2_webapp/home.html')

def about(request):
    return render(request, 'q2_webapp/about.html')

def contact(request):
    return render(request, 'q2_webapp/contact.html')
