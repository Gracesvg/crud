from django.shortcuts import render
from django.http import HttpResponse
from .models import People


# Create your views here.


def home(request):
    return render(request, 'index.html')


def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        school = request.POST.get('school')
        email = request.POST.get('email')

        person = People(name=name, email=email, school=school)
        person.save()

        # print(name, school)
        return HttpResponse("success")

def people(request):
    d=People.objects.all()
    context = {"data": d}
    return render(request,'People.html',context)
