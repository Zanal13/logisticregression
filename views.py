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
