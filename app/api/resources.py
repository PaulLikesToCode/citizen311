from tastypie import fields
from tastypie.resources import ModelResource
from app.models import Complaints, Comments

class Comments(ModelResource):
    class Meta:
        queryset = Comments.objects.all()
        resource_name = 'comment'

class Complaints(ModelResource):
    comments = fields.ToManyField(Comments, 'comment', full=True)

    class Meta:
        queryset = Complaints.objects.all()
        resource_name = 'complaint'