from tastypie.resources import ModelResource
from sps.models import Sps
from tastypie.authorization import Authorization

class SpsResource(ModelResource):
    class Meta:
        queryset = Sps.objects.all()
        resource_name = 'sps'
        authorization = Authorization()
        fields = ['song', 'content']