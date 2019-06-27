from django.shortcuts import render
from django.http import HttpResponse
from cmdb.models import cmdb

# Create your views here.

def get_property(request):
#    try:
        property = cmdb.objects.filter().values()
        return render(request, 'page_split.html', {'property': property})
#    except Exception as e:
#        return HttpResponse('this is test!')

