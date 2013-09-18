from django.http import HttpResponse
from django.shortcuts import render
from app.models import Complaints

def main(request):
#    get_JSON(request)
    complaint = Complaints.objects.all()
    data = {
        'complaint':complaint
    }

#    return HttpResponse("citizen311 home")
    print data
    return render(request, 'home.html', data)

