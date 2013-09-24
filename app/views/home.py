from django.http import HttpResponse
from django.shortcuts import render
from app.models import Complaints
from django.core import serializers

def main(request):
    complaint = serializers.serialize('json', Complaints.objects.all())
    data = {
        'complaint':complaint
    }
#    print data
    return render(request, 'home.html', data)

