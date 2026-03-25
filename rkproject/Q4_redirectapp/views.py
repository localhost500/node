from django.shortcuts import render, redirect

def page1(request):
    return render(request, 'Q4_redirectapp/page1.html')

def page2(request):
    return render(request, 'Q4_redirectapp/page2.html')

def go_to_page2(request):
    return redirect('page2')