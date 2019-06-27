from django.shortcuts import render
from django.http import HttpResponse
from cmdb.models import cmdb

# Create your views here.

def get_property(request):
#    try:
        all_property = cmdb.objects.filter()
        property = all_property.values()
        property_count = all_property.count()
        return render(request, 'page_split.html', {'property': property, 'property_count': property_count})
#    except Exception as e:
#        return HttpResponse('{}')

