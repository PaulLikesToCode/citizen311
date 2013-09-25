from django.shortcuts import render
from app.models import Complaints, Comments
from django.core import serializers
from django.contrib.auth.models import User


def main(request):
    all_info = list(Complaints.objects.all()) + list(Comments.objects.all())
    user_info = User.objects.select_related().only('username', 'id')
    json = serializers.serialize('json', all_info)
    print 'user_info_____________________'
    print user_info[0].email
#    assert isinstance(user_dict, object)
    return render(request, 'home.html', { 'json': json })

