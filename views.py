from django.http import JsonResponse
from django.shortcuts import render
from .models import Continent, Country, City

def get_countries(request):
    continent_id = request.GET.get('continent_id')
    countries = Country.objects.filter(continent_id=continent_id).order_by('name')
    country_list = []
    for country in countries:
        country_list.append({'id': country.id, 'name': country.name})
    return JsonResponse({'countries': country_list})

def get_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    city_list = []
    for city in cities:
        city_list.append({'id': city.id, 'name': city.name})
    return JsonResponse({'cities': city_list})

def index(request):
    if request.method=="POST":
        continent=request.POST['TB_continent']
        country=request.POST['TB_country']
        city=request.POST['TB_city']
        name=request.POST['fname']
        lname=request.POST['lname']
        print(continent)
        print(country)
        print(city)
        print(name)
        print(lname)
        country_selected= Country.objects.filter(pk=country)
        print(country_selected)
        for i in country_selected:
            print(i.name)
        city_selected = City.objects.filter(pk=city)
        print(city_selected)
    continents = Continent.objects.all().order_by('name')
    context = {'continents': continents}
    return render(request, 'index.html', context)




from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .forms import *

# Create your views here.
def mf_update_details(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            id=form.cleaned_data["registration_id"]
            print(id)
            return HttpResponse("You registartion is successful")
        else:
            pass
    else:
        form = RegistrationForm(auto_id=True)
        return render(request,"registration.html",{'form':form})
    

    
    
    
    
    from django.urls import path
from . import views
urlpatterns = [
path("mainframe/update_details",views.mf_update_details,name="update_details")
]







from django.db import models

# Create your models here.
class Registration(models.Model):
    registration_id=models.PositiveIntegerField()
    name=models.CharField(max_length=10)
    address = models.TextField()
    
    
    
    
    
    from .models import *
from django import forms

class RegistrationForm(forms.ModelForm):
    post_codes=(
        ('A',"534211"),
        ('B',"894063"),
    )
    postal_code = forms.ChoiceField(choices=post_codes,required=True)
    class Meta:
        model = Registration
        fields=[
            "registration_id",
            "address"
        ]
        labels={
            "registration_id":"Registration Id",
            
        }
        
        
        
        
        <form method="POST">
    {% csrf_token %} 
    {% for field in form %}
    {% if field.name == "address" %}
    <div class="a" style="color:red;">
    {{ field.label }}
    {{ field }}
    </div>
    {% else %}
    {{ field.label }}
    {{ field }}
    {% endif %}
    {% endfor %}


    <div>
        <button type="submit">Register</button>
    </div>
    
    
    
    
    
    from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("demo1.urls")),
]

