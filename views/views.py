from django.shortcuts import render
from myapp.models import Country, State, District

def dependantfield(request):
    countryid = request.GET.get('country', None)
    stateid = request.GET.get('state', None)
    state = None
    district = None
    if countryid:
        getcountry = Country.objects.get(id=countryid)
        state = State.objects.filter(country=getcountry)
    if stateid:
        getstate = State.objects.get(id=stateid)
        district = District.objects.filter(state=getstate)
    country = Country.objects.all()
    return render(request, 'dependantfield.html', locals())
