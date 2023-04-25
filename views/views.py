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

# import cx_Oracle

# # set up connection details
# dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLCDB.localdomain')
# conn = cx_Oracle.connect(user='myusername', password='mypassword', dsn=dsn_tns)

# # perform database operations
# cursor = conn.cursor()
# cursor.execute('SELECT * FROM mytable')
# results = cursor.fetchall()
# print(results)

# # close connection
# conn.close()
