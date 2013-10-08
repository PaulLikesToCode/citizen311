from django.shortcuts import render
from app.models import Complaints, Comments
from django.core import serializers
from django.contrib.auth.models import User
import requests


def main(request):
    all_info = list(Complaints.objects.all()) + list(Comments.objects.all())
    currentUrl = request.get_full_path()
    request.session['currentUrl'] = currentUrl
    print request.session['currentUrl']
    neighborhood_info = Complaints.objects.all().order_by('neighborhood')
    user_info = User.objects.select_related().only('username', 'id')
    json = serializers.serialize('json', all_info)
    data = {
        'json': json,
        'neighborhood_info': neighborhood_info
    }
    print 'user_info_____________________'
    print neighborhood_info[0].neighborhood
#    assert isinstance(user_dict, object)
    return render(request, 'home.html', data)

