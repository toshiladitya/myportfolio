from django.shortcuts import render
from .models import Guest
# Create your views here.
def portfolio(request):
    if request.method=="POST":
        name=request.POST.get('name')
        print(name)
        email=request.POST.get('email')
        print(email)
        subject=request.POST.get('subject')
        print(email)
        message=request.POST.get('message')
        print(message)
        data=Guest(name=name , email=email, subject=subject, message=message)
        data.save()
    return render(request,'index.html')
